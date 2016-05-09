from dataiku_census.models import CensusLearnSql


class Services(object):

    @staticmethod
    def get_model_fields_names():
        listing = []

        # We list all fields from the model object
        for field in CensusLearnSql._meta.fields:
            listing.append(field.get_attname_column()[1])

        # and remove the 'id' which is useless
        for i in range(len(listing) - 1):
            if listing[i] == 'id':
                del listing[0]

        return listing
