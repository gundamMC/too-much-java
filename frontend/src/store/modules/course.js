import $axios from '../../axios-instance';
import moment from "moment";

const state = {
    courseList: null,
    submissions: {},
    submissionsLoading: true
};

const mutations = {
    updateCourseList(state, newCourse){
        state.courseList = newCourse;
    },

    removeCourseList(state){
        state.courseList = null;
    },

    updateSubmissions(state, newSubmission){
        state.submissions = newSubmission;
    },

    startSubmissionsLoading(state){
        state.submissionsLoading = true;
    },

    finishSubmissionsLoading(state){
        state.submissionsLoading = false;
    },

};

const actions = {
    getCourses(context) {
        $axios
            .get('course/')
            .then(
                response => {

                    // update date format
                    for (let c = 0; c < response.data.length; c++) {
                        // for each course
                        for (let u = 0; u < response.data[c].units.length; u++){
                            // for each unit
                            for (let a = 0; a < response.data[c].units[u].assignments.length; a++){
                                // for each assignment
                                response.data[c].units[u].assignments[a].date = moment(response.data[c].units[u].assignments[a].date).format('dddd MMMM Do, YYYY');
                                response.data[c].units[u].assignments[a].due_date = moment(response.data[c].units[u].assignments[a].due_date).format('dddd MMMM Do, YYYY [at] h:mm:ss a');
                            }

                            for (let latest = 0; latest < response.data[c].units[u].latest.length; latest++){
                                // for each latest
                                response.data[c].units[u].latest[latest] = response.data[c].units[u].assignments.find(x => x.id === response.data[c].units[u].latest[latest])
                            }
                        }
                    }

                    context.commit('updateCourseList', response.data)

                }
            );
    },

    getSubmissions(context, assignment_id) {
        context.commit('startSubmissionsLoading');

        $axios
            .get('assignment/' +  assignment_id + '/submissions/')
            .then(
                response => {
                    // update submissions info
                    for (let i = 0; i < response.data.length; i++){
                        response.data[i].submitted_date = moment(response.data[i].submitted_date).format('dddd MMMM Do, YYYY [at] h:mm:ss a');
                    }

                    context.commit('updateSubmissions', response.data);
                }
            ).finally(context.commit('finishSubmissionsLoading'));
    },

    setSubmissions(context, submissions_data) {
        // used for updating raw data returned by grading new submissions
        for (let i = 0; i < submissions_data.length; i++){
            submissions_data[i].submitted_date = moment(submissions_data[i].submitted_date).format('dddd MMMM Do, YYYY [at] h:mm:ss a');
        }

        context.commit('updateSubmissions', submissions_data);
    }
};

const getters = {
    courses(state) {
        return state.courseList;
    },
    courseLoaded(state, getters) {
        return (getters.courses != null);
    },
    course: (state, getters) => (id) => {
        return getters.courses.find(thing => thing.id == id);  // don't really want to bother with DRF's type
      },
    unit: (state, getters) => (course_id, unit_id) => {
        return getters.course(course_id).units.find(x => x.id == unit_id);
    },
    assignment: (state, getters) => (course_id, unit_id, assignment_id) => {
        return getters.unit(course_id, unit_id).assignments.find(x => x.id == assignment_id);
    },
    submissions(state) {
        return state.submissions;
}
};

export default {
    state,
    getters,
    actions,
    mutations
}