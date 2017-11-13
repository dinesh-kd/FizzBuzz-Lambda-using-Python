import json
def lambda_handler(event, context):
    try:
        number = event['number']
        if event['range']:
            range_number = event['range']
        else:
            range_number = 0

        def getfizzbuzz(num):
            fizz = num % 2
            buzz = num % 3
            if fizz == 0 and buzz == 0:
                return 'FizzBuzz'
            elif fizz == 0:
                return 'Fizz'
            elif buzz == 0:
                return 'Buzz'
            else:
                return count

        count = number
        if range_number > 0:
            resp = {}
            while count < range_number:
                resp.update({count: getfizzbuzz(count)})
                count += 1
        else:
            resp = getfizzbuzz(number);

        return resp;
    except:
        return 'Invalid request'
