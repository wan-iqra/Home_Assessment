import os
import datetime
import subprocess
import webbrowser

# run pytest and generate report
def generateReport():
    # option 1: html-pytest
    # Create dynamic report filename with timestamp
    # timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # report_dir = "reports_html"
    # os.makedirs(report_dir, exist_ok=True)
    # report_path = os.path.join(report_dir, f"report_{timestamp}.html")
    #
    # try:
    #     print(f"Running tests... Saving HTML report to '{report_path}'")
    #     subprocess.run(["pytest", f"--html={report_path}", "--self-contained-html"])
    #
    #     print("Opening HTML report in browser...")
    #     webbrowser.open(f"file://{os.path.abspath(report_path)}")
    #
    # except subprocess.CalledProcessError as e:
    #     print(f"Command failed: {e}")
    # except FileNotFoundError:
    #     print("Make sure 'pytest' and 'pytest-html' are installed.")

    # option 2: allure-pytest
    # # Create a dynamic directory name using timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    allure_dir = f"reports_allure/{timestamp}"

    # Ensure directory exists (pytest will create it too, but for safety)
    os.makedirs(allure_dir, exist_ok=True)

    os.system(f"pytest --alluredir={allure_dir}")
    os.system(f"allure serve {allure_dir}")


# run main to run whole test suite
if __name__ == "__main__":
    generateReport()
    print("Press any key to exit")
