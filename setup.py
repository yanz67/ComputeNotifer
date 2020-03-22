import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="compute_notifier",
    version="0.0.1",

    description="Compute Notifier",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "compute_notifier"},
    packages=setuptools.find_packages(where="compute_notifier"),

    install_requires=[
        "aws-cdk.core==1.30.0",
        "aws-cdk.aws_lambda==1.30.0",
        "aws-cdk.aws_events==1.30.0",
        "aws-cdk.aws_sns==1.30.0",
        "aws-cdk.aws_sns_subscriptions==1.30.0",
        "aws-cdk.aws_events_targets==1.30.0",
        "aws-cdk.aws_iam==1.30.0",
        "boto3"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
