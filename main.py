import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Students fulfilling the Scheme guidelines of various Ministries are eligible toapply for these scholarships. These are available on the Home Page of the Portal.', ['Who','are','eligible','to','apply','for','Scholarship','Schemes'], required_words=['eligible' ,'apply' ])
    response('Closure dates for acceptance of various scholarship applications are available in the National Scholarships Portal', ['what', 'are', 'closure', 'dates'], required_words=['last', 'date','closure'])
    response('In order to apply online, please visit the website through URL www.scholarships.gov.in', ['how','can','I', 'apply', 'online'], required_words=['apply', 'online'])
    response('Applying procedures for Scholarship Schemes for both Fresh and Renewal aregiven below:Fresh:Student have to Click on the option “Student Login”, on the home page of NationalScholarships Portal. Fill up the application as per the instructions given by the system then click on save button. After saving, student will get a “Temporary ID”. The system will instruct the applicant to submit his/her Temporary ID and date of birth to fill subsequent details. Once registration is complete on click of submit button, a Permanent Registration ID is generated which can be used for Renewal and tracking the status of application Renewal: Renewal Students have to apply with their Application Id and Date of Birth which they registered previous year. Student can also use Forgot Application ID to retrieve their ID. Only those students would be able to Renew who had actually got the scholarships payments last year from NSP 1.0. ', ['how','to','submit','the','online','application?','should ','i','need','the','user','id','and','password'], required_words=['submit', 'online' , 'application'])
    response('All the information can be edited till the closure of application form. After final submission, your application will be forwarded to the next level and application hereby cannot be edited.', ['can',' i','edit','the','information','already','saved','up','to','what','time'], required_words=['saved', 'edit','already'])
    response('Fields provided with red asterisk (*) mark are mandatory fields.', ['which','feild','in','the','application','form','are','mandatory'], required_words=['which', 'field'])
    response('You should separately inform the mistakes detected by you to the Institute/District/Region/State. The software provides facility at the level of the Institute & State to edit & correct limited information.', ['what','happens','if','i','detect','mistakes','after','forwarding','the','application','to','the','next','level'], required_words=['mistakes','after','detect'])
    response('The Fields which can be edited are : Gender,Religion,Category,Profession,Annual Income,Aadhar Number,Disability,Day Scholar/Hostlar,Mode of Study,IFSC Code,Account No.,Admission Fees and Tution Fees.However, corrections made by the Institute/State, if any, would be conveyed instantly to the student through SMS/email.', ['which','field','institute','/state','can','edit'], required_words=['edit','field'] )
    response(' No. You can fill up the online application in as many sittings as you wish, until you are satisfied that you have entered all desirable fields correctly. The software provides facility to save your application at every stage.', ['do','i','have','to','fill','up','the','online','application','in','one','sitting'], required_words=['one' , 'sitting' 'fill'])
    response(' UID number otherwise known as ‘Aadhaar’ number is Unique Identification Number given by Unique Identification Authority of India (UIDAI). Aadhaar is unique 12 digit number assigned after de-duplication of biometrics.', ['what','is','UID','/Aadhar','number'], required_words=['uid', 'aadhar' , 'number'])
    response('adhaar No. is not Mandatory for the Students in order to Register and fill up the application form online. Students can apply for Scholarship without entering the Aadhaar no. but in that case they have to enter Aadhaar Enrollment Id. For the States of Aasam, Meghalya and Mizoram Aadhar Number is not mandatory.', ['do','i','need','to','get','my','aadhar','card','to','apply','for','scholarship'], required_words=['card', 'aadhar', 'scholarship'])
    response('Yes. An Application ID (Permanent ID) will be provided to the candidate once his/her Registration is done. It will be conveyed to candidates through SMS and e-mail. Students should memorize their Application ID as it will be required while applying for Fresh/renewal scholarship.', ['is','there','any','permanent','ID?','how','will','it','be','communicated','to','me'], required_words=['permanent', 'id'])
    response(' No, you cannot apply as a fresh if you are a Renewal candidate. Your application will be rejected in that case.', ['can','i','apply','as','a','fresh','if','i','am','a','renewal','candidate'], required_words=['fresh', 'renewal' , 'apply'])
    response('You should immediately approach the institute to contact with the nodal officer of the State where the institute is located. You can also approach the Nodal Officer of that State directly through e-mail under intimation to the Ministry. If your institute is an eligible institution, the State Government concerned would enter it into the database and then you can apply.', ['what','should','i','do','if','i','dont','find','any','institute','name','in','thr','drop','down','menu'], required_words=['institute', 'name' , 'drop','down','menu'])
    response('The name and contact details of the Nodal Officer/State Department of all States/UTs are available in Services->Know your State Nodal Officer option.', ['how','do','i','know','the','name','and','address','of','nodal ','officer','/state','department','of','my','state'], required_words=['nodal', 'officer', 'state'])
    response('Student can check the status of Online Application by submitting his/her Permanent id and Date Of Birth and open the link “Check your Status”.', ['how','to','check','the','status','of','my','application'], required_words=['check', 'status'])
    response(' You may click on Guidelines link of particular Scheme displaying in On-Boarded schemes section on the Home page.', ['how','to','view','the','details','of','a','paticular','scheme'], required_words=['details', 'scheme' , 'particular'])
    response('The deadline for verification of application at Institute/District/State Level will be displayed on portal as and when the dates are being closed.', ['how','know','the','deadline','verification','of','application','at','institute','/district','/state','level'], required_words=['verification', 'deadline'])
    response(' This procedure would be widely published as soon as the modalities are finalized.', ['would','there','be','a','procedure','for','publishing','advertisment','by','state','which','may','be','put','on','portal'], required_words=['publishing', 'advertisement'])
    response(' The “Forgot Application Id” option may be used and this problem can be overcome by using Search by Bank Account Number and Search by Mobile Number.', ['hoe','to','overcome','the','problem','of','login','even','after','getting','system','general','application','ID','and','DOB','as','passsword'], required_words=['forgot', 'application','id'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))

