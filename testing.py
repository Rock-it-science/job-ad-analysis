import unittest

from scraper import scrape
from search_ads import search
from text_preprocessing import preprocess
from analysis_functions import pos_tagging

class TestScraper(unittest.TestCase):
    # Note that most tests for the scraper are made using output from the function, which somewhat defeats the point of these tests.
    #  This important part is that I have looked at these outputs and verified that they make sense with the job results in browser.
    #  It is also worth running the tests to ensure consistency of these functions' outputs.

    def test_scraper(self):
        # The scrape function should return the job title and description for a given job ad link
        # Note that job ads get deleted, so this test may not pass in the future
        self.assertEquals(scrape("https://ca.indeed.com/viewjob?jk=80513b6ff37cc19d&tk=1fmmgbvjjnpqk800&from=serp&vjs=3"), ['Store Manager', "Claire's - A Career that's always in style\n\nStore Manager Opportunity\n\nAbout the Role\n\nAs Store Manager, your core area of responsibilities will be: Sales and profit - Achieving store targets through driving sales and more\nSales and profit: achieving store targets through driving sales\nCustomer service: delivering the finest level of customer service\nStore operations: keeping the store running smoothly\nCommerciality: Ensuring your store is well merchandised and commercially correct\nTeam leadership: recruiting, training, managing and providing direction and development to ensure your team are challenged and achieving results\nEar piercing (you will receive full training)\n\nAbout Claire's\n\nA leading high street fashion retailer with +3000 stores globally\nWe specialize in fashionable jewelry, accessories and cosmetics products\nOur core customer ranges from children to young women. We accommodate all our customers' moods, attitudes and styles, including: feminine and pretty, unique/individual and the latest catwalk trends\nWe are a fun place to work! We encourage all store members to wear our product\nWe encourage and support your development! If you're committed, ambitious and willing to learn we will provide you with the skills you need to grow in our company!\n\nAbout You\n\nHigh school diploma or equivalent required\n1 to 2 years retail management experience\nExcellent verbal/written communication and organizational skills\nBasic computer skills\nSound understanding of mathematics and strong reading comprehension skills\nUnderstands the importance of Customer Service\nAbility to analyze sales reports and strategically problem solve\nAbility to stand during scheduled shifts\nAbility to maneuver up to 25 lbs regularly and up to 75 lbs occasionally\nBending, stooping, extended reaching, climbing ladders and step stools while placing merchandise throughout the store and assisting Customers\nAbility to operate POS system\nClaire's is an equal opportunity employer committed to diversity, equity and inclusion and we encourage applications from members of all under represented groups, including those with disabilities. We will accommodate applicants' needs, upon request, throughout all stages of the recruitment process. Please inform us of the accommodation(s) that you may require. Information received relating to accommodation will be addressed confidentially. To request accommodation, please email Benefits@claires.com. Only messages sent for this purpose will be considered."])
        self.assertEquals(scrape("https://example.com/"), ['',''])
    
    def test_search_ads(self):
        # The search function returns a dict containing the job titles and descriptions for all ads in a Indeed search URL
        # This function is somewhat more difficult to test since it relies on all of the ads in a page staying consistent, but at the time of writing the below assertion passes 
        self.assertEquals(search("https://ca.indeed.com/plumber-jobs-in-Vernon,-BC?vjk=451d813b494d1af0"), {'https://ca.indeed.com/plumber-jobs-in-Vernon,-BC?vjk=451d813b494d1af0': [{'url': 'https://ca.indeed.com/viewjob?jk=3f7a52827f48d8f2&fccid=dcf79452c119abb3&vjs=3', 'title': 'Plumber Journeyperson - Kelowna', 'content': 'Gateway Mechanical currently has an exciting opportunity for a Journeyperson Plumber to assist the construction and service teams!\n\nThe plumber is responsible for installing new equipment and materials, performing new construction, renovations, repairs, and replacements for our valued clients.\n\nDuties:\n\nWork within the construction and service plumbing industry, specifically in a commercial setting\nTend to emergency service calls\nProvide excellent customer service and abide by all client/site specific guidelines\nSolder, thread pipe, take accurate measurements and interpret isometric drawings\nInstall new equipment and materials\nComplete the required daily equipment inspections, safety reports, and Field Level Hazard Assessments\nRead and interpret blueprints\nOther duties as assigned\n\nSkills:\n\nSafety conscious\nAttention to detail\nExperience with basic Commercial plumbing and heating systems such as domestic water, hydronic heating, drainage and venting\nExercise sound judgement and maintain a professional demeanor\nStrong technical expertise\nAbility to work well under pressure, individually and as part of a team in a multi-trade environment\nAbility to take the correct initiative and work independently while maintaining clear communication to overseeing Foreman\n\nExperience & Qualifications:\n\nJourneyperson Plumber Certification\nExperience in the construction industry\nExperience handling emergency calls\nValid class 5 driver’s license\nValid safety certifications such as First Aid, WHMIS, TDG, CSTS, PSTS, Fall Protection, AWP, H2S Alive, considered an asset\n\nThe Future is Bright. Come Grow with Us!\nhttp://careers.gatewaymechanical.ca/'}]})

class TestPreProcessing(unittest.TestCase):
    def test_preprocessing(self):
        # Preprocessing is the easiest function to test since it has easy and consistent text inputs
        self.assertEquals(preprocess('ABC123'), 'abc ')
        self.assertEquals(preprocess('a\nb\nc'), 'a b c')
        self.assertEquals(preprocess('abc...\n  abc:cba'), 'abc. abc cba')

class TestNLPFunctions(unittest.TestCase):
    def test_nlpfunctions(self):
        # Assert one of each type of skill phrase
        # Noun phrase
        self.assertEquals(pos_tagging('Developing machine learning models.'), ['machine learning'])
        
        # Verb phrase
        self.assertEquals(pos_tagging('object oriented programming skills.'), ['object object', 'object orient'])

        # Nount Gerund
        self.assertEquals(pos_tagging('strong problem solving skills.'), ['strong problem', 'strong solving', 'problem solve'])

if __name__ == '__main__':
    unittest.main()