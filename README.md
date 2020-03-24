# Compute Notifier

Compute Notifier stack will provision Cloud Watch event trigger, lambda and an SNS topic.
The event trigger will be triggered based on the cron expression which will trigger the lambda
that will push SNS notification if there are any EC2 instances running in the AWS account.  
The configuration is defined in `cdk.json`  

## Provisioning Compute Notifier
* Define your configuration in `cdk.json`
    * Make sure to at add least one email for notifications
    * Update `schedule_expression` to define when is the event triggered
        * https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
* Bootstrap  
`cdk --profile $AWS_PROFILE bootstrap`
* synth  
`cdk --profile $AWS_PROFILE synth`
* deploy  
`cdk --profile $AWS_PROFILE deploy`
* destroy  
`cdk --profile $AWS_PROFILE destroy`  

You can set deployment environment by setting environment variable `DEPLOY_ENVIRONMENT`  
`DEPLOY_ENVIRONMENT=prod cdk --profile $AWS_PROFILE synth`  
Default environment is `dev`

### Adding Auxiliary Configuration
The `cdk.json` configuration can be overwritten per invironment by adding a config file into
the `aux_config` folder.  The name of the file should be `{env}.json`  
The structure of aux config should be:  

```json
{
  "emails": [
    "email address"
  ],
  "schedule_expression": "cron(* 18 ? * * *)"
}
``` 


### Notes
Cron time is in GMT

#### Requirements
* AWS CDK  
`npm install -g aws-cdk`
* Node.js >= 10.3.0
* Python >= 3.6 
* Create python virtual env
    * `python3 -m venv .env`
* Run pip3 to install required modules
    * `pip3 install .`