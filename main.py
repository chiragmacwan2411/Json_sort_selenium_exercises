from tests import test_two, test_one

def solution():

    # TEST - 1 : input "test_results.json"
    print("STARTING TEST - 1 \n")
    ans_1 = test_one.analyze_json("resources/test_results.json")
    ans_1.test_json()



    # TEST - 2
    print("STARTING TEST - 2 \n")
    ans_2 = test_two.selenium_test()
    ans_2.test_selenium()

if __name__ == '__main__':
    solution()