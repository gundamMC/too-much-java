import org.junit.platform.launcher.Launcher;
import org.junit.platform.launcher.LauncherDiscoveryRequest;
import org.junit.platform.launcher.TestPlan;
import org.junit.platform.launcher.TestIdentifier;
import org.junit.platform.launcher.core.LauncherDiscoveryRequestBuilder;
import org.junit.platform.launcher.core.LauncherFactory;
import org.junit.platform.launcher.listeners.SummaryGeneratingListener;
import org.junit.platform.launcher.listeners.TestExecutionSummary;

import java.util.List;
import java.util.Set;
import org.json.*;

import static org.junit.platform.engine.discovery.DiscoverySelectors.selectClass;

public class testController {

    public static void main(String[] args){

        LauncherDiscoveryRequest request = LauncherDiscoveryRequestBuilder.request()
                .selectors(
                        selectClass(tester.class)
                )
                .build();

        Launcher launcher = LauncherFactory.create();

        //discover all tests for use later
        TestPlan plan = launcher.discover(request);
        Set<TestIdentifier> testIdentifiers = plan.getChildren("[engine:junit-jupiter]/[class:tester]");  // get all tests in tester

        // System.out.println("==================");

        // Register a listener of your choice
        SummaryGeneratingListener listener = new SummaryGeneratingListener();
        launcher.registerTestExecutionListeners(listener);

        launcher.execute(request);

        TestExecutionSummary summary = listener.getSummary();

        List<TestExecutionSummary.Failure> failures = summary.getFailures();

        // System.out.println("Testing hello world:");

        // System.out.println("Success: " + summary.getTestsSucceededCount());
        // failures.forEach(failure -> System.out.println("failure - " +
        //         failure.getTestIdentifier().getDisplayName() + " - " + failure.getException()));

        JSONObject values = new JSONObject();
        values.put("points", summary.getTestsSucceededCount());
        values.put("total", summary.getTestsFoundCount());
        
        // create an array of tests
        JSONArray tests = new JSONArray();

        int failsFound = 0;
        long failedTotal = summary.getTestsFailedCount();

        for (TestIdentifier test : testIdentifiers) {
                // System.out.println("Test: " + test.getDisplayName() + " - " + test.getUniqueId());
                JSONObject detail = new JSONObject();
                detail.put("name", test.getDisplayName());

                Boolean passed = true;
                String details = "Successful";

                if (failsFound < failedTotal){
                        for (TestExecutionSummary.Failure failure : failures) {
                                if (failure.getTestIdentifier().getUniqueId().equals(test.getUniqueId())){
                                        passed = false;
                                        details = failure.getException().getMessage();
                                        failsFound++;
                                        break;
                                }
                        }
                } 
                detail.put("passed", passed);
                detail.put("details", details);

                
                tests.put(detail);
        }

        values.put("tests", tests);

        System.out.println(values.toString());  // pass JSON dict to python

    }

}
