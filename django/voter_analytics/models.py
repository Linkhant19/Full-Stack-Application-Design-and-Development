from django.db import models
import datetime

# Create your models here.

class Voter(models.Model):
    '''
    store and represent one voter from Newton, MA. 
    *    Last Name
    *    First Name
    *    Residential Address - Street Number
    *    Residential Address - Street Name
    *    Residential Address - Apartment Number
    *    Residential Address - Zip Code
    *    Date of Birth
    *    Date of Registration
    *    Party Affiliation
    *    Precinct Number
    *    v20state
    *    v21town
    *    v21primary
    *    v22general
    *    v23town
    *    voter_score is a numeric value, indicating how many of the past 5 elections the voter participated in
    '''
    last_name = models.TextField()
    first_name = models.TextField()
    street_number = models.IntegerField()
    street_name = models.TextField()
    apartment_number = models.TextField()
    zip_code = models.IntegerField()
    date_of_birth = models.DateField()
    date_of_registration = models.DateField()
    party_affiliation = models.TextField()
    precinct_number = models.IntegerField()
    v20state = models.TextField()
    v21town = models.TextField()
    v21primary = models.TextField()
    v22general = models.TextField()
    v23town = models.TextField()
    voter_score = models.IntegerField()

    def __str__(self):
        '''Return a string representation of this model instance'''
        return f"{self.last_name}, {self.first_name} ({self.street_number}, {self.street_name}, {self.zip_code}) {self.date_of_birth} {self.party_affiliation} {self.voter_score}"

def load_data():
    '''Load the data records from CSV file, create Django model instances.'''

    # delete all records:
    # because for this app, we want to start with an empty database
    # this can be dangerous
    Voter.objects.all().delete()

    filename = '/Users/linix/Desktop/newton_voters.csv'
    f = open(filename, 'r')

    # discard the first line containing header
    headers = f.readline()

    # go through the entire file one line at a time

    for line in f:
        try:
            fields = line.split(',')

            # "parsing": splitting some data into fields, assign each to variable
            # create a new instance of Result object with this record from CSV
            result = Voter(last_name=fields[1],
                            first_name=fields[2],
                            street_number=fields[3],
                            street_name=fields[4],
                            apartment_number=fields[5],
                            zip_code=fields[6],
                            date_of_birth=datetime.datetime.strptime(fields[7], '%Y-%m-%d').date(),
                            date_of_registration=datetime.datetime.strptime(fields[8], '%Y-%m-%d').date(),
                            party_affiliation=fields[9].strip(),
                            precinct_number=fields[10],
                            v20state=fields[11],
                            v21town=fields[12],
                            v21primary=fields[13],
                            v22general=fields[14],
                            v23town=fields[15],
                            voter_score=fields[16]
                        )
            print(f'Created result: {result}')
            result.save() # save/commit to the database
        except: 
            print(f'Error processing line {line}')
    print(f'Done. Created {len(Voter.objects.all())} Results.')