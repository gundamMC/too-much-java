import os
import shutil
import zipfile
from datetime import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.utils.timezone import make_aware

from grader.models import CodeFileAssignment, Unit
from too_much_java.settings.base import MEDIA_ROOT


@staff_member_required
def dropoff(request):
    if 'file' not in request.FILES:
        # no file uploaded, show default page
        return render(request, '../templates/assignment_dropoff.html')
    else:
        f = request.FILES['file']
        file_name = f.name
        # takes a zip file with each assignment in its subfolders
        try:
            with zipfile.ZipFile(f) as unzipped:

                # extract zip
                zip_dir = os.path.join(MEDIA_ROOT, 'dropoff', file_name)

                if os.path.exists(zip_dir) and len(os.listdir(zip_dir)) > 0:
                    # clear and override files if there are already ones
                    shutil.rmtree(zip_dir)

                unzipped.extractall(zip_dir)
        except zipfile.BadZipFile:
            # unexpcted exception
            return render(request, '../templates/assignment_dropoff.html',
                          {'error': 'file {0} is not a valid zip file'.format(file_name)})

        created_assignments = []

        assignment_dirs = os.listdir(zip_dir)
        # filter to only directories
        assignment_dirs = [x for x in assignment_dirs if os.path.isdir(x)]

        if len(assignment_dirs) < 1:
            return render(request, '../templates/assignment_dropoff.html',
                          {'error': 'No valid assignment folder found'})

        for item in assignment_dirs:
            # path of sub directory (i.e. root of assignment)
            path = os.path.join(zip_dir, item)

            subitems = os.listdir(path)

            if 'info.txt' not in subitems:
                return render(request, '../templates/assignment_dropoff.html',
                              {'error': 'info.txt not found in {0}'.format(path)})

            if 'tester.java' not in subitems:
                return render(request, '../templates/assignment_dropoff.html',
                              {'error': 'tester.java not found in {0}'.format(path)})

            # tries to gather template files
            # a zip file has priority
            if 'template.zip' in subitems:
                code_template = os.path.join(path, 'template.zip')
            else:
                # otherwise, try to gather java files and zip them
                java_files = [java_file for java_file in subitems if java_file.endswith('.java')]
                if len(java_files) > 1:
                    java_files.remove('tester.java')
                    with zipfile.ZipFile(os.path.join(path, 'template.zip'), 'w') as template_zip:
                        for f in java_files:
                            template_zip.write(os.path.join(path, f))
                    code_template = os.path.join(path, 'template.zip')
                else:
                    # no template file found, skipping it
                    code_template = None

            # start to read assignment info
            with open(os.path.join(path, 'info.txt')) as info:
                info_lines = info.read().splitlines()

            if len(info_lines) < 8:
                return render(request, '../templates/assignment_dropoff.html',
                              {'error': '{0} has only {1} lines, but expecting >= 8'
                                  .format(os.path.join(path, 'info.txt'), len(info_lines))
                               })

            # info_lines:
            # [0] = name
            # [1] = description
            # [2] = unit id
            # [3] = post date
            # [4] = due date
            # [5] = total points
            # [6] = attempts
            # [=>7] = markdown instruction

            # parse dates
            try:
                date = datetime.strptime(info_lines[3], '%m/%d/%Y %H:%M:%S')
                date = make_aware(date)
                due_date = datetime.strptime(info_lines[4], '%m/%d/%Y %H:%M:%S')
                due_date = make_aware(due_date)
            except ValueError as e:
                print(e)
                return render(request, '../templates/assignment_dropoff.html',
                              {'error': 'date of {0} does not match format %m/%d/%Y %H:%M:%S'
                                        ' | Example: 08/26/2023 23:59:00'.format(path)})

            # parse ints
            try:
                unit_id = int(info_lines[2])
                points = int(info_lines[5])
                attempts = int(info_lines[6])
            except ValueError:
                return render(request, '../templates/assignment_dropoff.html',
                              {'error': 'unit id / point / attempts is not integer in {0}'.format(path)})

            test = dict(
                name=info_lines[0],
                description=info_lines[1],
                unit=unit_id,
                date=date,
                due_date=due_date,
                points=points,
                attempts=attempts,
                instructions='\n'.join(info_lines[7:]),
                code_template=code_template,
                tester_path=os.path.join(path, 'tester.java')
            )

            print(test)

            # finally, create the object
            assignment = CodeFileAssignment(
                name=info_lines[0],
                description=info_lines[1],
                unit=Unit.objects.get(pk=unit_id),
                date=date,
                due_date=due_date,
                points=points,
                attempts=attempts,
                instructions='\n'.join(info_lines[7:]),
                code_template=code_template,
                tester_path=os.path.join(path, 'tester.java')
            )

            assignment.save()

            created_assignments.append(assignment.name)
            print(created_assignments)

        print('final ===============')
        print(file_name)
        print(created_assignments)
        return render(request, '../templates/assignment_dropoff.html',
                      {'name': file_name, 'created_assignments': created_assignments})
