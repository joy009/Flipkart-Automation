def create_summary_report(file_name, result):
    write_to_file(file_name, result)


def write_to_file(write_file_name, result):
    html_str = "<h3>MeetNotes Automation Testcase Summary</h3><table border=1><tr><th align='left' " \
               "style='padding: 5px 5px 5px 5px;'>Test-cases</th><th style='padding: 5px 5px 5px 5px;'>Count</th>"
    rows_name = ["Total", "Successful", "Failures", "Errors", "Skipped"]

    for row_name, test_count in zip(rows_name, result):
        html_str += "<tr><th align='left' style='padding: 5px 5px 5px 5px;'>" + row_name + \
                    "</th><td align='center'>" + str(test_count) + "</td></tr>"
    html_str += "</table>"

    Html_file = open(write_file_name, "w+")
    Html_file.write(html_str)
    Html_file.close()