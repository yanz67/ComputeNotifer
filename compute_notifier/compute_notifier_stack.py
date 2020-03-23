from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_sns as sns,
    aws_sns_subscriptions as sns_subscriptions,
    aws_events as events,
    aws_events_targets as events_targets,
    aws_iam as iam,
)


class ComputeNotifierStack(core.Stack):
    def __init__(self, scope: core.Construct,
                 id: str,
                 deploy_env: str,
                 aux_config: {},
                 **kwargs):
        super().__init__(scope, id, **kwargs)

        env_settings = self.node.try_get_context(deploy_env) or {}

        if aux_config:
            env_settings.update(aux_config)

        if not env_settings:
            raise Exception(f'Configuration for {deploy_env} environment not found')

        notifier_topic = sns.Topic(self,
                                   id=f'{deploy_env}-computeNotifierTopic',
                                   display_name='Compute Notifier Topic',
                                   topic_name=f'{deploy_env}-ComputeNotifier')
        for email in env_settings['emails']:
            notifier_topic.add_subscription(sns_subscriptions.EmailSubscription(email))

        notifier_lambda = _lambda.Function(self, f'{deploy_env}-computeNotifierLambda',
                                           handler='compute_notifier.handler',
                                           runtime=_lambda.Runtime.PYTHON_3_8,
                                           code=_lambda.Code.asset('functions'),
                                           environment={
                                               'COMPUTE_NOTIFIER_TOPIC_ARN': notifier_topic.topic_arn,
                                               'ENVIRONMENT_NAME': deploy_env
                                           })
        notifier_topic.grant_publish(notifier_lambda)

        notifier_lambda.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=['ec2:DescribeInstances']
        ))

        notifier_rule = events.Rule(self,
                                    f'{deploy_env}-computeNotifierRule',
                                    schedule=events.Schedule.expression(env_settings['schedule_expression']))
        notifier_rule.add_target(events_targets.LambdaFunction(notifier_lambda))
