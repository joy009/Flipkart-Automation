import xml.etree.ElementTree as ET

total_pass = 0
total_failure = 0
total_error = 0
total_count = 0
total_time = 0


def create_full_report(html_file, xml_file, start_time, end_time, successful_test_cases, failure_test_cases,
                       error_test_cases):

    # Read all lines of report.xml file
    f = open(xml_file, 'r')
    lines = f.readlines()
    f.close()

    # Update report.xml file to remove xml version line
    # Also add the root as <testsuites>
    # f = open(xml_file, "w")
    # xml_line = "<?xml version=\"1.0\" ?>"+"\n"
    # f.write("<testsuites>\n")
    #
    # for line in lines:
    #     if line!=xml_line:
    #         f.write(line)
    # f.write("</testsuites>")
    # f.close()

    tree = ET.parse(xml_file)
    root = tree.getroot()
    total_execution_time = str(end_time - start_time)

    html_str = "<h3>MeetNotes Automation Testcase Summary</h3>" \
               "<b>Start Time: </b>" + str(start_time) + "<br>" + \
               "<b>End Time:  </b>" + str(end_time) + "<br>" + \
               "<b>Duration: </b>" + total_execution_time + "<br>" + \
               "<b>Status: </b> Pass " + str(successful_test_cases) + " Failure " + str(failure_test_cases) +\
               " Error " + str(error_test_cases) + "<br><br>" \
               "<table border=1 cellspacing=0 cellpadding=0><tr bgcolor=#C0C0C0><th align='left' " \
               "style='padding: 5px 5px 5px 5px;'>Test Group/Test case</th>" \
               "<th style='padding: 5px 5px 5px 5px;'>Count</th>" \
               "<th style='padding: 5px 5px 5px 5px;'>Pass</th>" \
               "<th style='padding: 5px 5px 5px 5px;'>Fail</th>" \
               "<th style='padding: 5px 5px 5px 5px;'>Error</th>" \
               "<th style='padding: 5px 5px 5px 5px;'>Execution Time</th></tr>"

    def _add_testsuite_class(testsuite, html_str):
        global total_count, total_error, total_pass, total_failure, total_time
        suite_name = testsuite.get('name').split('-')[0]
        suite_total_tests = testsuite.get('tests')
        suite_errors = testsuite.get('errors')
        suite_failures = testsuite.get('failures')
        suite_execution_time = testsuite.get('time')
        suite_pass = str(int(suite_total_tests) - int(suite_errors) - int(suite_failures))

        total_count += int(suite_total_tests)
        total_failure += int(suite_failures)
        total_error += int(suite_errors)
        total_pass += int(suite_pass)
        total_time += float(suite_execution_time)

        if int(suite_failures) + int(suite_errors) == 0:
            bgcolor = "bgcolor=#00FF00"
        else:
            bgcolor = "bgcolor=#FF0000"

        html_str += "<tr " + bgcolor + "><td> " + suite_name + " </td><td align='center'>" + suite_total_tests + \
                    "</td><td align='center'>" + suite_pass + "</td><td align='center'>" + suite_failures + \
                    "</td><td align='center'>" + suite_errors + "</td><td align='center'>" + suite_execution_time + "</tr>"
        return html_str

    def _add_testcase(test, html_str):
        test_name = test.get('name')
        test_execution_time = test.get('time')
        if len(test.getchildren()) > 0:
            if "failure" in test.getchildren()[0].tag:
                color = "style='color:red;'"
            else:
                color = "style='color:brown;'"
            message = test.find(".//").text
        else:
            message = "pass"
            color = "style='color:green;'"
        html_str += "<tr><td "  + color + "><ul><li>" + str(test_name) + "</td>"
        if "red" in color:
            html_str += "<td align='center' style='overflow-y:scroll' colspan='4'><div " + \
                        color + "> failure </div><div style='width: 500px; " \
                        "height: 100px'>" + str(message) + \
                    "</div></td><td align='center'>" + test_execution_time + "</td></tr>"

        elif "brown" in color:
            html_str += "<td align='center' style='overflow-y:scroll' colspan='4'><div " + \
                        color + "> error </div>" "<div style='width: 500px; " \
                        "height: 100px'>" + str(message) + \
                    "</div></td><td align='center'>" + test_execution_time + "</td></tr>"
        else:
            html_str += "<td align='center' colspan='4'>"  + str(message) + "</td><td align='center'>" \
                        + test_execution_time + "</td></tr>"
        return html_str

    for testsuite in root.iter('testsuite'):
        html_str = _add_testsuite_class(testsuite, html_str)
        for test in testsuite.iter('testcase'):
            html_str = _add_testcase(test, html_str)

    html_str += "<tr><th>Total</th><th align='center'>" + str(total_count) + "</th><th align='center'>" + \
                str(total_pass) + "</th><th align='center'>" + str(total_failure) + "</th><th align='center'>" \
                + str(total_error) + "</th><th>" + str(total_time) + "</tr></table>"
    html_str += "</table>"
    Html_file = open(html_file, "w+")
    Html_file.write(html_str)
    Html_file.close()
