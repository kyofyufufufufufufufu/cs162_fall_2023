from house import House

# both tests will be ran through pytest testhouse.py to confirm whether they are a succesful/failed test

#positive test
def test_sqfeet():
    housetest = House()
    expectedhousetest = housetest.get_sq_feet()
    # housetest.get_sq_feet()
    expected_total_sqfeet = 400

    assert expected_total_sqfeet == housetest.get_sq_feet()

test_sqfeet() # <<< this receives a positive test, showing that our expected value equals the actual value

#negative test

def test_sqfeet2():
    housetest = House()
    expectedhousetest = housetest.get_sq_feet()
    # housetest.get_sq_feet()
    expected_total_sqfeet = 300

    assert expected_total_sqfeet == housetest.get_sq_feet()

test_sqfeet2() #<<< this receives a failed test, showing one error that assert 300 != the actual value of 400 square feet


#python -n pytest to test
#include expected_lockdoor = value oupt
#expected_lights_on_off = value output

#assert expected_variable == House.lockdoor()
#assert expected_lights_on_off == House.lights_on_off()