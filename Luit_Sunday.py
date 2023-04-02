# 1) Create a list of services using Python.

# 2) The list should be empty initially.

amz_services = []

# 3) Populate the list using append or insert.

amz_services.append('lambda')
amz_services.append('dynamodb')
amz_services.append('rds')
amz_services.append('ec2')
amz_services.append('s3')
amz_services.append('iam')

# 4) Print the list and the length of the list.

print(amz_services)
print(len(amz_services))

# 5) Remove two specific services from the list by name or by index

amz_services.remove('rds')
amz_services.remove('s3')

# 6) Print the new list and the new length of the list

print(amz_services)
print(len(amz_services))

# 7) Push your code to GitHub and include the link in your LinkedIn write up

