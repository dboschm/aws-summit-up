from aws_cdk import Stack
from constructs import Construct

from aws_cdk.aws_lambda_python_alpha import PythonFunction
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as apigateway
from aws_cdk import aws_dynamodb as ddb
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets

class InfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # DynamoDB Table
        table = ddb.Table(
            self, "MyTable",
            partition_key=ddb.Attribute(name="id", type=ddb.AttributeType.STRING),
            stream=ddb.StreamViewType.NEW_IMAGE
        )

        # Lambda Function to interact with DynamoDB
        lambda_function = PythonFunction(
            self, "MyFunction",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="handler",
            entry="../service",
            index="lambda_handler.py"
        )

        # Grant the Lambda function read/write permissions on the table
        table.grant_read_write_data(lambda_function)

        # API Gateway integration
        api = apigateway.LambdaRestApi(
            self, "MyEndpoint",
            handler=lambda_function
        )

        # Example of granting the lambda role read privileges to the table
        table.grant_read_data(lambda_function)

        # # Lambda Function as an EventBridge target
        # event_lambda = _lambda.Function(
        #     self, "EventBridgeLambda",
        #     runtime=_lambda.Runtime.PYTHON_3_12,
        #     handler="event_handler.handler",
        #     code=_lambda.Code.from_asset("lambda"),
        #     environment={
        #         "TABLE_NAME": table.table_name
        #     }
        # )

        # # Set up the EventBridge rule
        # rule = events.Rule(
        #     self, "Rule",
        #     event_pattern={
        #         "source": ["aws.dynamodb"],
        #         "detail-type": ["DynamoDB Stream Record"],
        #         "detail": {
        #             "eventName": ["INSERT", "MODIFY"]
        #         }
        #     }
        # )

        # # Add the lambda function as the target of the rule
        # rule.add_target(targets.LambdaFunction(event_lambda))