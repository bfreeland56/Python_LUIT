import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

response = table.put_item(
Item = { 
     'Name': 'Kelvin Galabuzi',
     'Email': 'kelvingalabuzi@handson.cloud',
     
     'Name': 'Jackie Galabuzi',
     'Email': 'jackiegalabuzi@handson.cloud',
     
     'Name': 'Tony Galabuzi',
     'Email': 'tonygalabuzi@handson.cloud',
     
     'Name': 'Raymond Galab',
     'Email': 'raymondgalab@handson.cloud',
     
     'Name': 'Brian Jones',
     'Email': 'brianjones@handson.cloud',
     
     'Name': 'Dinae Galabuzi',
     'Email': 'dinaegalabuzi@handson.cloud',
     
     'Name': 'Hussein Galeb',
     'Email': 'husseingaleb@handson.cloud',
     
     'Name': 'Cory labuzi',
     'Email': 'corylabuzi@handson.cloud',
     
     'Name': 'Tory Galabuzi',
     'Email': 'torygalabuzi@handson.cloud',
     
     'Name': 'Hanna Galabuzi',
     'Email': 'hannagalabuzi@handson.cloud',
       }
       
)
print("PutItem succeeded:")