from utilities import json_reader
import json

class analyze_json:

    """
        class constructor
    """
    def __init__(self, my_json_file):
        self.json_file = my_json_file


    """
           reads the json file and returns python dict
    """
    def json_helper(self):
        try:
            json_dict = json_reader.json_data_key_reader(self.json_file, "test_suites")
            return json_dict
        except KeyError:
            print("Error while reading the Key")
        except ValueError:
            print("ValueError::Error while reading json")
        except TypeError:
            print("TypeError::Error while reading json")



    """
           analyze the dict and prepares final result json to print
           STEPS:
           --> sorts the passed, failed and blocked TCs suite wise
           --> updates temporary tracker list
           --> updates final result with updating respective suite name
           --> converts to json to be printed
    """
    def test_json(self):
        my_json = self.json_helper()
        result = []

        for suite in my_json:
            suite_names = [[{"passed": 0}], [{"failed": 0}], [{"blocked": 0}], [{"tc_took_more_than_10s": 0}]]

            # added sort by 'test_name' key
            sorted_tcs = sorted(suite["results"], key=lambda k: k['test_name'])

            for test_case in sorted_tcs:
                if (test_case["status"] == "pass"):
                    suite_names[0][0]["passed"] += 1
                    suite_names[0].append(test_case)
                elif (test_case["status"] == "fail"):
                    suite_names[1][0]["failed"] += 1
                    suite_names[1].append(test_case)
                else:
                    suite_names[2][0]["blocked"] += 1

                    # below line should be uncommented, if details of blocked cases needs to shown in result
                    # suite_names[2].append(test_case)

                if (test_case["time"]!= '') and (float(test_case["time"]) > 10):
                    suite_names[3][0]["tc_took_more_than_10s"] += 1


            result.append({suite["suite_name"]:suite_names})

        result = json_reader.json_dumper(result)


        print(result)