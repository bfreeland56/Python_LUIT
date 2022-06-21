AWS Service Inventory


Create a list of services using Python. IE: S3, Lambda, EC2, etc
1. The list should be empty initially.
2. Populate the list using append or insert.
3. Print the list and the length of the list. 
4. Remove two specific services from the list by name or by index.
5. Print the new list and the new length of the list.




#!/usr/bin/env python3.7

# Python Implementation here

# create a variable to hold a place in memory for the list of AWS services

aws_services = []

print(aws_services)

# using 'append' method, add an object to the list
aws_services.append('vpn')
aws_services.append('autoscaling')
aws_services.append('cloudfront')
aws_services.append('cloudtrail')
aws_services.append('cloudwatch')
aws_services.append('rds')

print(aws_services)

# print the list and the length of the list
print(len(aws_services))

# remove 2 services from the list by name
aws_services.remove('cloudtrail')
aws_services.remove('cloudwatch')

print(aws_services)

# print the list and the length of the list
print(len(aws_services))

print(aws_services)