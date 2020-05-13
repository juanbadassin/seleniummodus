## Run the tests
In order to run the tests, we just need to have docker and docker-compose installed. 
Wheather we are runnign in localhost or in a CI instance, we just need those two.

The tests are triggered by running `run_tests.sh` which tears down the environment if it's running,
and then it spin a new environment up. 

The test environment is made of a test runner, chrome and firefox containers.

We should export the env variable BROWSER pointing to either `chrome` or `firefox` before running the tests

When running in a CI, both chrome and firefox would be run in parallel

We could use different configs to run the tests. As of know, there's only one configuration
file, which is `TEST.cfg` but we could add as many as we want, to point to different environments

The tests produce two artifacts, a junit report, which can be later on taken by CI plugins to 
present it on a user friendly way and screenshots, which can help us to debug when something fails


## Scenarios

The test scenarios would be split in two:

* Budget
* Reports

### Budget scenarios:
- Verify that adding a new inflow increases the total inflow
- Verify that adding a new outflow increases the total outflow
- Verify that the working balance matches the inflow - outflow
- Verify that new items can be added to the table
- Verify that only numbers can be entered as value
- Verify that utf-8 chars are accepted in the description
- Verify that the totals in the Amount colum matches the totals in the bottom for both inflow and outflow
- Verify that an item can be updated (category, description and value)
- Verify that an item can be deleted
- Verify that only positive numbers can be saved when editing Income items
- Verify that only negative numbers can be saved when editing non income items

### Report scenarios

- Verify that the total inflow matches the number in the budget tab
- Verify that the total outflow matches the number in the budget tab
- Verify that outflow by category add up to the list of items added by category in the budget tab. Here we 
add more than one item by category and we verify that they add up in the reports tab
- Verify that the totals by category in inflow vs outflow match the totals in spending by category 