#!/bin/bash

echo "Running Custom Module Tests..."

behave features/03Customer.feature --no-capture --no-capture-stderr -f allure_behave.formatter:AllureFormatter -o allure-results
allure generate allure-results --clean -o allure-report
open allure-report/index.html
