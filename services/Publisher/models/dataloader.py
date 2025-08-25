
from models.logger import get_logger
from sklearn.datasets import fetch_20newsgroups
log = get_logger()
class DataLoader:


    @staticmethod
    def get_all() -> dict[str , list]:
        

        interesting_cats=['alt.atheism',
        'comp.graphics',
        'comp.os.ms-windows.misc',
        'comp.sys.ibm.pc.hardware',
        'comp.sys.mac.hardware',
        'comp.windows.x',
        'misc.forsale',
        'rec.autos',
        'rec.motorcycles',
        'rec.sport.baseball']

        not_interesting_cats=['rec.sport.hockey',
        'sci.crypt',
        'sci.electronics',
        'sci.med',
        'sci.space',
        'soc.religion.christian',
        'talk.politics.guns',
        'talk.politics.mideast',
        'talk.politics.misc',
        'talk.religion.misc']

        newsgroups_interesting=fetch_20newsgroups(subset='all',categories=interesting_cats)
        newsgroups_not_interesting=fetch_20newsgroups(subset='all',categories=not_interesting_cats)
        newsgroups_interesting = [i for i in newsgroups_interesting.data]
        newsgroups_not_interesting = [i for i in newsgroups_not_interesting.data]


        data = {"interesting" :newsgroups_interesting , "not_interesting":newsgroups_not_interesting}
        
        log.info(f"get a data len = interesting:{len(data["interesting"])} not_interesting:{len(data['not_interesting'])} ")

        return data

