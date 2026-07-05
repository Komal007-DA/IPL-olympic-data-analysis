import pandas as pd
import streamlit as st
import functionfile
import matplotlib.pyplot as plt
import seaborn as sns
import figurs

batsman=['SC Ganguly', 'BB McCullum', 'RT Ponting', 'DJ Hussey',
       'Mohammad Hafeez', 'R Dravid', 'W Jaffer', 'V Kohli', 'JH Kallis',
       'CL White', 'MV Boucher', 'B Akhil', 'AA Noffke', 'P Kumar',
       'Z Khan', 'SB Joshi', 'PA Patel', 'ML Hayden', 'MEK Hussey',
       'MS Dhoni', 'SK Raina', 'JDP Oram', 'S Badrinath', 'K Goel',
       'JR Hopes', 'KC Sangakkara', 'Yuvraj Singh', 'SM Katich',
       'IK Pathan', 'T Kohli', 'YK Pathan', 'SR Watson', 'M Kaif',
       'DS Lehmann', 'RA Jadeja', 'M Rawat', 'D Salunkhe', 'SK Warne',
       'SK Trivedi', 'G Gambhir', 'V Sehwag', 'S Dhawan', 'L Ronchi',
       'ST Jayasuriya', 'DJ Thornely', 'RV Uthappa', 'PR Shah',
       'AM Nayar', 'SM Pollock', 'Harbhajan Singh', 'S Chanderpaul',
       'LRPL Taylor', 'AC Gilchrist', 'Y Venugopal Rao', 'VVS Laxman',
       'A Symonds', 'RG Sharma', 'SB Styris', 'AS Yadav', 'SB Bangar',
       'WPUJC Vaas', 'RP Singh', 'WP Saha', 'LR Shukla',
       'DPMD Jayawardene', 'S Sohal', 'B Lee', 'PP Chawla', 'WA Mota',
       'Kamran Akmal', 'Shahid Afridi', 'DJ Bravo', 'MA Khote', 'A Nehra',
       'GC Smith', 'Pankaj Singh', 'RR Sarwan', 'S Sreesanth',
       'VRV Singh', 'SS Tiwary', 'DS Kulkarni', 'R Vinay Kumar',
       'AB Agarkar', 'M Kartik', 'I Sharma', 'AM Rahane', 'Shoaib Malik',
       'MK Tiwary', 'KD Karthik', 'R Bhatia', 'MF Maharoof', 'VY Mahesh',
       'TM Srivastava', 'B Chipli', 'DW Steyn', 'DB Das', 'MK Pandey',
       'HH Gibbs', 'DNT Zoysa', 'D Kalyankrishna', 'SE Marsh',
       'SA Asnodkar', 'Sohail Tanvir', 'Salman Butt', 'BJ Hodge',
       'Umar Gul', 'AB Dinda', 'SP Fleming', 'S Vidyut', 'JA Morkel',
       'AB de Villiers', 'LPC Silva', 'DB Ravi Teja', 'Misbah-ul-Haq',
       'YV Takawale', 'RR Raje', 'PJ Sangwan', 'Mohammad Asif',
       'GD McGrath', 'Joginder Sharma', 'MS Gony', 'M Muralitharan',
       'M Ntini', 'DT Patil', 'A Kumble', 'S Anirudha', 'MM Patel',
       'CK Kapugedera', 'A Chopra', 'T Taibu', 'J Arunkumar', 'PP Ojha',
       'SP Goswami', 'SR Tendulkar', 'U Kaul', 'TM Dilshan', 'A Mishra',
       'AD Mascarenhas', 'NK Patel', 'LA Pomersbach', 'Iqbal Abdulla',
       'Younis Khan', 'PM Sarvesh Kumar', 'DP Vijaykumar',
       'Shoaib Akhtar', 'Abdur Razzak', 'H Das', 'DR Smith', 'SD Chitnis',
       'CRD Fernando', 'VS Yeligati', 'L Balaji', 'A Mukund', 'RR Powar',
       'JP Duminy', 'A Flintoff', 'T Thushara', 'JD Ryder',
       'KP Pietersen', 'T Henderson', 'Kamran Khan', 'RS Bopara',
       'CH Gayle', 'MC Henriques', 'R Bishnoi', 'FH Edwards', 'KV Sharma',
       'PC Valthaty', 'RJ Quiney', 'AS Raut', 'Yashpal Singh', 'M Manhas',
       'AA Bilakhia', 'AN Ghosh', 'BAW Mendis', 'DL Vettori',
       'MN van Wyk', 'RE van der Merwe', 'TL Suman', 'Shoaib Ahmed',
       'GR Napier', 'KP Appanna', 'LA Carseldine', 'NV Ojha',
       'SM Harwood', 'M Vijay', 'SB Jakati', 'DA Warner', 'RJ Harris',
       'D du Preez', 'M Morkel', 'AD Mathews', 'J Botha', 'C Nanda',
       'SL Malinga', 'Mashrafe Mortaza', 'A Singh', 'GJ Bailey',
       'AB McDonald', 'Y Nagar', 'SS Shaikh', 'R Ashwin',
       'Mohammad Ashraful', 'CA Pujara', 'OA Shah', 'Anirudh Singh',
       'Jaskaran Singh', 'AP Tare', 'AT Rayudu', 'R Sathish', 'R McLaren',
       'AA Jhunjhunwala', 'P Dogra', 'A Uniyal', 'MS Bisla', 'YA Abdulla',
       'EJG Morgan', 'JM Kemp', 'S Tyagi', 'RS Gavaskar', 'SE Bond',
       'KA Pollard', 'S Ladda', 'DP Nannes', 'MJ Lumb', 'DR Martyn',
       'S Narwal', 'AB Barath', 'Bipul Sharma', 'FY Fazal', 'AC Voges',
       'MD Mishra', 'UT Yadav', 'J Theron', 'SJ Srivastava', 'R Sharma',
       'Mandeep Singh', 'KM Jadhav', 'SW Tait', 'KB Arun Karthik',
       'KAJ Roach', 'PD Collingwood', 'CK Langeveldt', 'VS Malik',
       'A Mithun', 'AP Dole', 'AN Ahmed', 'RS Sodhi', 'DE Bollinger',
       'S Sriram', 'B Sumanth', 'C Madan', 'AG Paunikar', 'MR Marsh',
       'AJ Finch', 'STR Binny', 'Harmeet Singh', 'IR Jaggi',
       'DT Christian', 'RV Gomez', 'MA Agarwal', 'AUK Pathan',
       'UBT Chand', 'DJ Jacobs', 'Sunny Singh', 'NJ Rimmington',
       'AL Menaria', 'WD Parnell', 'JJ van der Wath', 'R Ninan',
       'S Aravind', 'MS Wade', 'TD Paine', 'SB Wagh', 'AC Thomas',
       'JEC Franklin', 'Shakib Al Hasan', 'DH Yagnik', 'S Randiv',
       'BJ Haddin', 'NLTC Perera', 'NL McCullum', 'JE Taylor',
       'J Syed Mohammad', 'RN ten Doeschate', 'TR Birt', 'AG Murtaza',
       'Harpreet Singh', 'M Klinger', 'AC Blizzard', 'I Malhotra',
       'L Ablish', 'CA Ingram', 'S Nadeem', 'P Parameswaran',
       'CJ Ferguson', 'VR Aaron', 'AA Chavan', 'ND Doshi', 'B Kumar',
       'Y Gnaneswara Rao', 'S Rana', 'BA Bhatt', 'F du Plessis',
       'RE Levi', 'GJ Maxwell', 'SPD Smith', 'MN Samuels', 'SA Yadav',
       'KK Cooper', 'JP Faulkner', 'HV Patel', 'DAJ Bracewell',
       'DJ Harris', 'Ankit Sharma', 'SP Narine', 'GB Hogg', 'RR Bhatkal',
       'CJ McKay', 'N Saini', 'DA Miller', 'Azhar Mahmood', 'P Negi',
       'RJ Peterson', 'KMDN Kulasekara', 'A Ashish Reddy',
       'V Pratap Singh', 'BB Samantray', 'MJ Clarke', 'Gurkeerat Singh',
       'AP Majumdar', 'PA Reddy', 'K Upadhyay', 'P Awana', 'AD Russell',
       'A Chandila', 'CA Lynn', 'Sunny Gupta', 'MC Juneja', 'KK Nair',
       'GH Vihari', 'MDKJ Perera', 'R Shukla', 'B Laughlin', 'AS Rajpoot',
       'M Vohra', 'JD Unadkat', 'Mohammed Shami', 'BMAJ Mendis',
       'R Rampaul', 'CH Morris', 'SV Samson', 'SMSM Senanayake',
       'BJ Rohrer', 'KL Rahul', 'Q de Kock', 'R Dhawan', 'MG Johnson',
       'LJ Wright', 'IC Pandey', 'CM Gautam', 'X Thalaivan Sargunam',
       'DJG Sammy', 'KW Richardson', 'MM Sharma', 'UA Birla',
       'Parvez Rasool', 'Sandeep Sharma', 'S Kaul', 'Sachin Baby',
       'PV Tambe', 'NM Coulter-Nile', 'CJ Anderson', 'NJ Maddinson',
       'AR Patel', 'JJ Bumrah', 'JDS Neesham', 'TG Southee', 'MA Starc',
       'BR Dunk', 'RR Rossouw', 'Shivam Sharma', 'YS Chahal',
       'LMP Simmons', 'VH Zol', 'BCJ Cutting', 'Imran Tahir',
       'BE Hendricks', 'S Gopal', 'M de Lange', 'R Tewatia', 'JO Holder',
       'Karanveer Singh', 'SS Iyer', 'DJ Hooda', 'Anureet Singh',
       'KS Williamson', 'SA Abbott', 'J Suchith', 'RG More', 'HH Pandya',
       'D Wiese', 'SN Khan', 'MJ McClenaghan', 'DJ Muthuswami',
       'PJ Cummins', 'SN Thakur', 'JC Buttler', 'CR Brathwaite',
       'MP Stoinis', 'Ishan Kishan', 'C Munro', 'P Sahu', 'KH Pandya',
       'AD Nath', 'MJ Guptill', 'KJ Abbott', 'TM Head', 'M Ashwin',
       'NS Naik', 'RR Pant', 'SW Billings', 'KC Cariappa',
       'PSP Handscomb', 'Swapnil Singh', 'J Yadav', 'UT Khawaja',
       'HM Amla', 'F Behardien', 'BB Sran', 'A Zampa', 'N Rana',
       'S Kaushik', 'ER Dwivedi', 'CJ Jordan', 'TS Mills', 'A Choudhary',
       'BA Stokes', 'JJ Roy', 'Vishnu Vinod', 'Basil Thampi', 'CR Woakes',
       'RA Tripathi', 'DL Chahar', 'V Shankar', 'Rashid Khan',
       'RD Chahar', 'LH Ferguson', 'C de Grandhomme', 'AF Milne',
       'S Badree', 'Mohammad Nabi', 'AJ Tye', 'K Rabada', 'Kuldeep Yadav',
       'Washington Sundar', 'DM Bravo', 'AR Bawne', 'SP Jackson',
       'Ankit Soni', 'TA Boult', 'E Lewis', 'MA Wood', 'RK Singh',
       'DJM Short', 'K Gowtham', 'TK Curran', 'M Markande', 'B Stanlake',
       'Mujeeb Ur Rahman', 'A Dananjaya', 'Shubman Gill', 'Shivam Mavi',
       'Mohammed Siraj', 'H Klaasen', 'RK Bhui', 'JC Archer', 'PP Shaw',
       'LE Plunkett', 'Mustafizur Rahman', 'AD Hales', 'MK Lomror',
       'DR Shorey', 'MM Ali', 'M Prasidh Krishna', 'P Chopra',
       'JPR Scantlebury-Searles', 'Abhishek Sharma', 'IS Sodhi',
       'SO Hetmyer', 'S Dube', 'Navdeep Saini', 'JM Bairstow', 'KMA Paul',
       'Rasikh Salam', 'N Pooran', 'P Ray Barman', 'SM Curran',
       'GC Viljoen', 'Avesh Khan', 'S Lamichhane', 'HF Gurney', 'SD Lad',
       'AS Joseph', 'R Parag', 'MJ Santner', 'JL Denly', 'LS Livingstone',
       'KK Ahmed', 'AJ Turner', 'Harpreet Brar', 'SE Rutherford',
       'Y Prithvi Raj', 'P Simran Singh', 'JL Pattinson', 'A Nortje',
       'T Banton', 'D Padikkal', 'YBK Jaiswal', 'RD Gaikwad',
       'TU Deshpande', 'Abdul Samad', 'PK Garg', 'JR Philippe',
       'Kartik Tyagi', 'KL Nagarkoti', 'CV Varun', 'I Udana',
       'Ravi Bishnoi', 'Shahbaz Ahmed', 'AT Carey', 'N Jagadeesan',
       'T Natarajan', 'P Dubey', 'SS Cottrell', 'Arshdeep Singh',
       'DR Sams', 'M Jansen', 'RM Patidar', 'KA Jamieson',
       'M Shahrukh Khan', 'JA Richardson', 'Lalit Yadav', 'Virat Singh',
       'FA Allen', 'C Sakariya', 'DJ Malan', 'KS Bharat', 'PWH de Silva',
       'VR Iyer', 'GD Phillips', 'GHS Garton', 'AK Markram', 'K Yadav',
       'T Shamsi', 'NT Ellis', 'RV Patel', 'TL Seifert',
       'Anmolpreet Singh', 'Anuj Rawat', 'TH David', 'DP Conway',
       'Tilak Varma', 'R Powell', 'PBB Rajapaksa', 'RA Bawa', 'OF Smith',
       'A Badoni', 'PVD Chameera', 'A Manohar', 'R Shepherd', 'DJ Willey',
       'D Pretorius', 'JM Sharma', 'VG Arora', 'Mukesh Choudhary',
       'Umran Malik', 'D Brevis', 'B Sai Sudharsan', 'Ramandeep Singh',
       'HE van der Dussen', 'SS Prabhudessai', 'Akash Deep',
       'JR Hazlewood', 'KR Sen', 'Aman Hakim Khan', 'HR Shokeen',
       'Yash Dayal', 'DJ Mitchell', 'Shashank Singh', 'B Indrajith',
       'Harshit Rana', 'Mohsin Khan', 'Simarjeet Singh', 'M Theekshana',
       'AS Roy', 'Fazalhaq Farooqi', 'K Kartikeya', 'RP Meredith',
       'KS Sharma', 'T Stubbs', 'R Sanjay Yadav', 'A Tomar', 'PN Mankad',
       'OC McCoy', 'Sikandar Raza', 'Rahmanullah Gurbaz', 'KR Mayers',
       'Mukesh Kumar', 'HC Brook', 'AU Rashid', 'C Green', 'N Wadhera',
       'Arshad Khan', 'Abishek Porel', 'Dhruv Jurel', 'MG Bracewell',
       'MW Short', 'Mohit Rathee', 'YV Dhull', 'Yudhvir Singh',
       'Atharva Taide', 'Liton Das', 'PD Salt', 'Vijaykumar Vyshak',
       'Abdul Basith', 'Arjun Tendulkar', 'JP Behrendorff', 'AJ Hosein',
       'Naveen-ul-Haq', 'Noor Ahmad', 'JE Root', 'KM Asif', 'MD Shanaka',
       'Sanvir Singh', 'Vivrant Sharma', 'DG Nalkande']

bowler=['P Kumar', 'Z Khan', 'AA Noffke', 'JH Kallis', 'SB Joshi',
       'CL White', 'AB Dinda', 'I Sharma', 'AB Agarkar', 'SC Ganguly',
       'LR Shukla', 'B Lee', 'S Sreesanth', 'JR Hopes', 'IK Pathan',
       'K Goel', 'PP Chawla', 'WA Mota', 'JDP Oram', 'MS Gony',
       'M Muralitharan', 'P Amarnath', 'Joginder Sharma', 'GD McGrath',
       'B Geeves', 'MF Maharoof', 'R Bhatia', 'DL Vettori', 'MM Patel',
       'SR Watson', 'SK Trivedi', 'SK Warne', 'YK Pathan', 'D Salunkhe',
       'R Vinay Kumar', 'B Akhil', 'A Nehra', 'SM Pollock', 'DS Kulkarni',
       'ST Jayasuriya', 'Harbhajan Singh', 'AM Nayar', 'M Kartik',
       'Mohammad Hafeez', 'DJ Hussey', 'WPUJC Vaas', 'RP Singh',
       'SB Styris', 'SB Bangar', 'A Symonds', 'PP Ojha', 'Pankaj Singh',
       'Mohammad Asif', 'VY Mahesh', 'Shahid Afridi', 'DJ Bravo',
       'VS Yeligati', 'MA Khote', 'D Kalyankrishna', 'VRV Singh',
       'Sohail Tanvir', 'A Kumble', 'DNT Zoysa', 'SD Chitnis',
       'Yuvraj Singh', 'Shoaib Malik', 'DW Steyn', 'JA Morkel',
       'CRD Fernando', 'V Kohli', 'V Sehwag', 'Gagandeep Singh',
       'Y Venugopal Rao', 'Umar Gul', 'PJ Sangwan', 'M Ntini',
       'DP Vijaykumar', 'DB Ravi Teja', 'LPC Silva', 'DJ Thornely',
       'RR Raje', 'SK Raina', 'S Vidyut', 'L Balaji', 'CK Kapugedera',
       'DR Smith', 'AD Mascarenhas', 'A Mishra', 'Shoaib Akhtar',
       'Iqbal Abdulla', 'RR Powar', 'PM Sarvesh Kumar', 'Abdur Razzak',
       'RA Jadeja', 'TM Dilshan', 'RG Sharma', 'A Nel', 'BAW Mendis',
       'T Thushara', 'A Flintoff', 'SL Malinga', 'Kamran Khan',
       'T Henderson', 'JD Ryder', 'DP Nannes', 'AM Salvi', 'YA Abdulla',
       'VS Malik', 'FH Edwards', 'Harmeet Singh', 'CH Gayle',
       'MC Henriques', 'KP Pietersen', 'LRPL Taylor', 'RS Bopara',
       'MK Tiwary', 'Anureet Singh', 'RR Bose', 'KP Appanna',
       'Shoaib Ahmed', 'BJ Hodge', 'SR Tendulkar', 'RE van der Merwe',
       'JP Duminy', 'S Tyagi', 'GR Napier', 'SM Harwood', 'AS Raut',
       'SB Jakati', 'D du Preez', 'RJ Harris', 'TL Suman', 'A Singh',
       'M Morkel', 'LA Carseldine', 'A Mithun', 'C Nanda', 'SS Sarkar',
       'AD Mathews', 'AM Rahane', 'J Botha', 'Mashrafe Mortaza',
       'AB McDonald', 'Y Nagar', 'CK Langeveldt', 'R Ashwin', 'RA Shaikh',
       'Jaskaran Singh', 'SW Tait', 'A Uniyal', 'AA Jhunjhunwala',
       'R McLaren', 'AG Murtaza', 'R Sathish', 'RS Gavaskar', 'JM Kemp',
       'S Ladda', 'Bipul Sharma', 'SE Bond', 'KA Pollard', 'S Narwal',
       'UT Yadav', 'SJ Srivastava', 'AC Voges', 'R Sharma', 'J Theron',
       'NLTC Perera', 'KAJ Roach', 'PD Collingwood', 'C Ganapathy',
       'MB Parmar', 'SB Wagh', 'DE Bollinger', 'JD Unadkat', 'AP Dole',
       'AN Ahmed', 'FY Fazal', 'MR Marsh', 'L Ablish', 'S Sriram',
       'AJ Finch', 'STR Binny', 'ND Doshi', 'TG Southee', 'S Randiv',
       'AL Menaria', 'DT Christian', 'AUK Pathan', 'RV Gomez',
       'JEC Franklin', 'AC Thomas', 'WD Parnell', 'M Manhas',
       'NJ Rimmington', 'RN ten Doeschate', 'S Nadeem', 'BA Bhatt',
       'JJ van der Wath', 'S Aravind', 'R Ninan', 'Shakib Al Hasan',
       'PC Valthaty', 'S Dhawan', 'J Syed Mohammad', 'VR Aaron',
       'NL McCullum', 'JE Taylor', 'KMDN Kulasekara', 'P Parameswaran',
       'I Malhotra', 'B Chipli', 'B Kumar', 'AA Kazi', 'Anand Rajan',
       'P Prasanth', 'Y Gnaneswara Rao', 'AA Chavan', 'S Rana',
       'JP Faulkner', 'SS Mundhe', 'RW Price', 'GJ Maxwell', 'M de Lange',
       'MN Samuels', 'KK Cooper', 'DAJ Bracewell', 'HV Patel',
       'Ankit Sharma', 'DJ Harris', 'TP Sudhindra', 'F du Plessis',
       'SP Narine', 'GB Hogg', 'RR Bhatkal', 'P Awana', 'V Pratap Singh',
       'CJ McKay', 'AD Russell', 'A Ashish Reddy', 'Azhar Mahmood',
       'A Chandila', 'P Negi', 'LJ Wright', 'RJ Peterson', 'R Shukla',
       'MJ Clarke', 'BW Hilfenhaus', 'SPD Smith', 'K Upadhyay',
       'Sunny Gupta', 'MG Johnson', 'JJ Bumrah', 'S Badree', 'AS Rajpoot',
       'B Laughlin', 'GH Vihari', 'Mohammed Shami', 'BMAJ Mendis',
       'CH Morris', 'S Kaul', 'R Dhawan', 'MM Sharma', 'R Rampaul',
       'KV Sharma', 'SMSM Senanayake', 'JO Holder', 'IC Pandey',
       'Sandeep Sharma', 'YS Chahal', 'DJG Sammy', 'KW Richardson',
       'P Suyal', 'PV Tambe', 'BJ Rohrer', 'Parvez Rasool', 'MG Neser',
       'NM Coulter-Nile', 'AC Gilchrist', 'CJ Anderson', 'MA Starc',
       'JDS Neesham', 'AR Patel', 'M Vijay', 'R Tewatia', 'SA Yadav',
       'Shivam Sharma', 'Imran Tahir', 'V Shankar', 'LMP Simmons',
       'BCJ Cutting', 'K Santokie', 'S Gopal', 'BE Hendricks',
       'PJ Cummins', 'JW Hastings', 'Karanveer Singh', 'DJ Muthuswami',
       'TA Boult', 'SA Abbott', 'KC Cariappa', 'DJ Hooda', 'J Suchith',
       'RG More', 'D Wiese', 'MJ McClenaghan', 'HH Pandya', 'SN Thakur',
       'GS Sandhu', 'Gurkeerat Singh', 'J Yadav', 'BB Sran', 'M Ashwin',
       'C Munro', 'CR Brathwaite', 'MP Stoinis', 'P Sahu',
       'Mustafizur Rahman', 'AF Milne', 'Kuldeep Yadav', 'KH Pandya',
       'KJ Abbott', 'T Shamsi', 'S Kaushik', 'SM Boland', 'Swapnil Singh',
       'CJ Jordan', 'A Zampa', 'Sachin Baby', 'N Rana', 'DL Chahar',
       'KS Williamson', 'TS Mills', 'A Choudhary', 'TM Head',
       'Rashid Khan', 'BA Stokes', 'CR Woakes', 'T Natarajan',
       'RD Chahar', 'B Stanlake', 'Tejas Baroka', 'Basil Thampi',
       'C de Grandhomme', 'AJ Tye', 'LH Ferguson', 'Mohammad Nabi',
       'Mohammed Siraj', 'K Rabada', 'Washington Sundar', 'SS Agarwal',
       'NB Singh', 'RA Tripathi', 'Ankit Soni', 'MJ Henry', 'Avesh Khan',
       'MA Wood', 'M Markande', 'Mujeeb Ur Rahman', 'K Khejroliya',
       'K Gowtham', 'DJM Short', 'TK Curran', 'A Dananjaya',
       'Shivam Mavi', 'JC Archer', 'LE Plunkett', 'IS Sodhi', 'MK Lomror',
       'L Ngidi', 'KM Asif', 'DJ Willey', 'M Prasidh Krishna', 'MM Ali',
       'JPR Scantlebury-Searles', 'S Lamichhane', 'CJ Dala', 'KK Ahmed',
       'Navdeep Saini', 'S Dube', 'Rasikh Salam', 'KMA Paul', 'SM Curran',
       'CV Varun', 'GC Viljoen', 'Mandeep Singh', 'P Ray Barman',
       'MJ Santner', 'JP Behrendorff', 'SC Kuggeleijn', 'AS Joseph',
       'HF Gurney', 'S Midhun', 'R Parag', 'LS Livingstone', 'SN Khan',
       'Abhishek Sharma', 'Arshdeep Singh', 'SE Rutherford',
       'Harpreet Brar', 'Y Prithvi Raj', 'O Thomas', 'AS Roy',
       'S Sandeep Warrier', 'JL Pattinson', 'SS Cottrell', 'Ravi Bishnoi',
       'A Nortje', 'I Udana', 'TU Deshpande', 'KL Nagarkoti',
       'Kartik Tyagi', 'DR Sams', 'Shahbaz Ahmed', 'Abdul Samad',
       'JR Hazlewood', 'DA Warner', 'CJ Green', 'P Dubey', 'Monu Kumar',
       'KA Jamieson', 'M Jansen', 'C Sakariya', 'JA Richardson',
       'RP Meredith', 'LI Meriwala', 'Lalit Yadav', 'Jalaj S Saxena',
       'FA Allen', 'PWH de Silva', 'Umran Malik', 'Akash Singh',
       'GD Phillips', 'AK Markram', 'GHS Garton', 'VR Iyer', 'K Yadav',
       'NT Ellis', 'RV Patel', 'IC Porel', 'AU Rashid', 'OF Smith',
       'Akash Deep', 'PVD Chameera', 'Mohsin Khan', 'R Shepherd',
       'Mukesh Choudhary', 'D Pretorius', 'VG Arora', 'YBK Jaiswal',
       'Tilak Varma', 'DG Nalkande', 'M Theekshana', 'D Brevis',
       'R Powell', 'KR Sen', 'Yash Dayal', 'Shashank Singh',
       'Aman Hakim Khan', 'OC McCoy', 'HR Shokeen', 'A Badoni',
       'DJ Mitchell', 'Harshit Rana', 'SS Iyer', 'K Kartikeya',
       'Simarjeet Singh', 'Fazalhaq Farooqi', 'R Sai Kishore',
       'Ramandeep Singh', 'PH Solanki', 'M Pathirana', 'R Sanjay Yadav',
       'J Little', 'RS Hangargekar', 'Sikandar Raza', 'Mukesh Kumar',
       'KR Mayers', 'NA Saini', 'RJW Topley', 'MG Bracewell',
       'Arshad Khan', 'C Green', 'Yash Thakur', 'Suyash Sharma',
       'SSB Magala', 'Mohit Rathee', 'MW Short', 'Vijaykumar Vyshak',
       'Yudhvir Singh', 'Arjun Tendulkar', 'D Jansen', 'Noor Ahmad',
       'Naveen-ul-Haq', 'Mayank Dagar', 'Gurnoor Brar', 'AJ Hosein',
       'Akash Madhwal', 'R Goyal', 'T Stubbs', 'Vivrant Sharma',
       'JE Root', 'Nithish Kumar Reddy', 'H Sharma']

death_players=('SA Yadav', 'Y Nagar', 'RA Tripathi', 'S Sreesanth', 'BA Stokes', 
            'G Gambhir', 'SE Rutherford', 'Harbhajan Singh', 'R Parag', 'JO Holder', 'B Kumar',
            'MV Boucher', 'SP Goswami', 'V Shankar', 'RD Gaikwad', 'MR Marsh', 'AN Ahmed', 
            'Mohammad Nabi','KC Sangakkara', 'TM Head', 'R Dhawan', 'JC Archer', 'JJ Bumrah', 
            'MA Agarwal', 'MS Gony', 'AM Rahane', 'RV Uthappa', 'Basil Thampi', 'BB McCullum',
            'NV Ojha', 'S Nadeem', 'DA Warner', 'HV Patel', 'M Morkel', 'SS Tiwary', 'M Rawat', 
            'GJ Maxwell', 'PVD Chameera', 'Gurkeerat Singh', 'DA Miller', 'Azhar Mahmood', 
            'Ankit Sharma', 'NLTC Perera', 'CJ Jordan', 'Ishan Kishan', 'LR Shukla', 'DG Nalkande',
            'SN Thakur', 'RG Sharma', 'S Anirudha', 'Y Venugopal Rao', 'JR Hazlewood', 'N Wadhera',
            'Abdul Samad', 'AR Patel','DH Yagnik', 'K Rabada', 'SV Samson', 'AJ Tye', 'M Vijay', 
            'GH Vihari', 'Mohammed Shami', 'TK Curran', 'AM Nayar',
            'CK Kapugedera', 'HR Shokeen', 'TA Boult', 'K Kartikeya','JEC Franklin',
            'SK Raina','SPD Smith','KL Rahul', 'Noor Ahmad', 'Sandeep Sharma','A Mishra','DW Steyn',
            'P Negi','DJ Bravo','MJ McClenaghan','Navdeep Saini',
            'Sohail Tanvir', 'AP Tare','H Klaasen','Shubman Gill','M Vohra','AS Rajpoot',
            'SO Hetmyer','E Lewis','SN Khan','SS Iyer','R Vinay Kumar','STR Binny','V Sehwag',
            'S Dhawan','GJ Bailey','Kuldeep Yadav','KH Pandya','MK Tiwary',
            'AD Mathews', 'Shakib Al Hasan', 'B Sumanth','P Kumar', 'KK Nair', 
            'CL White', 'JA Morkel', 'PWH de Silva','V Kohli', 'Shahbaz Ahmed', 'AS Raut', 
            'A Ashish Reddy', 'MF Maharoof', 'SP Narine', 'SK Trivedi', 'DJG Sammy',
            'EJG Morgan', 'Karanveer Singh', 'RM Patidar', 'WP Saha', 'SM Curran', 
            'RJ Harris', 'CH Morris', 'DR Smith','MG Johnson', 'OA Shah', 'A Kumble', 
            'R Ashwin', 'PP Ojha', 'Abhishek Sharma', 'RS Bopara', 'Yuvraj Singh','PJ Sangwan',
            'Z Khan', 'J Suchith', 'Bipul Sharma', 'MC Henriques', 'VR Aaron', 'ER Dwivedi',
            'R Dravid','KS Williamson', 'B Sai Sudharsan', 'AD Russell', 'S Aravind', 'OC McCoy',
            'B Lee', 'F du Plessis', 'KM Jadhav','M Manhas','Mohammed Siraj','DPMD Jayawardene',
            'JDP Oram','K Gowtham','SB Jakati','CRD Fernando','IK Pathan','Tilak Varma','D Wiese',
            'RR Powar','MK Lomror','RD Chahar','M Kartik','JP Behrendorff','SC Ganguly','KMA Paul',
            'KP Pietersen','Iqbal Abdulla','MA Starc','RA Jadeja','Sachin Baby','BB Samantray',
            'AB de Villiers','JP Faulkner','Rashid Khan','N Rana','MS Dhoni','S Gopal','CR Brathwaite',
            'RP Singh','DT Christian','D WieseHV Patel', 'I Sharma', 'LH Ferguson', 'DJ Hooda', 
            'SE Marsh', 'A Symonds', 'S Badrinath', 'R Tewatia', 'BCJ Cutting', 'TM Dilshan',
            'RN ten Doeschate', 'R Sathish', 'Mandeep Singh', 'TL Suman', 'J Syed Mohammad', 'MEK Hussey', 
            'KD Karthik', 'TG Southee', 'N Pooran', 'JP Duminy','PJ Cummins','DB Das','CJ Anderson',
            'SK Warne','DB Ravi Teja','AJ Finch', 'DJ Hussey','JPR Scantlebury-Searles','R Sharma','BJ Hodge',
            'JH Kallis','R Bhatia','Washington Sundar','AA BilakhiaHH Gibbs', 'AL Menaria', 'CH Gayle', 
            'Shivam Mavi', 'DS Kulkarni', 'J Botha', 'SR Watson', 'MK Pandey',
            'PP Chawla','C de Grandhomme','MP Stoinis','JC Buttler','SR Tendulkar',
            'A Nehra','WA MotaRR Powar','AB Agarkar','UT Yadav', 'Harmeet Singh', 
            'YK Pathan', 'AT Rayudu', 'AB McDonald', 'DL Vettori', 'MM Sharma', 'HH Pandya',
            'SL Malinga', 'KA Pollard', 'KV Sharma', 'MM Ali', 'LRPL Taylor', 'RR Pant')

venue=['M Chinnaswamy Stadium',
       'Punjab Cricket Association Stadium, Mohali', 'Feroz Shah Kotla',
       'Wankhede Stadium', 'Eden Gardens', 'Sawai Mansingh Stadium',
       'Rajiv Gandhi International Stadium, Uppal',
       'MA Chidambaram Stadium, Chepauk', 'Dr DY Patil Sports Academy',
       'Newlands', "St George's Park", 'Kingsmead', 'SuperSport Park',
       'Buffalo Park', 'New Wanderers Stadium', 'De Beers Diamond Oval',
       'OUTsurance Oval', 'Brabourne Stadium',
       'Sardar Patel Stadium, Motera', 'Barabati Stadium',
       'Brabourne Stadium, Mumbai',
       'Vidarbha Cricket Association Stadium, Jamtha',
       'Himachal Pradesh Cricket Association Stadium', 'Nehru Stadium',
       'Holkar Cricket Stadium',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Subrata Roy Sahara Stadium',
       'Maharashtra Cricket Association Stadium',
       'Shaheed Veer Narayan Singh International Stadium',
       'JSCA International Stadium Complex', 'Sheikh Zayed Stadium',
       'Sharjah Cricket Stadium', 'Dubai International Cricket Stadium',
       'Punjab Cricket Association IS Bindra Stadium, Mohali',
       'Saurashtra Cricket Association Stadium', 'Green Park',
       'M.Chinnaswamy Stadium',
       'Punjab Cricket Association IS Bindra Stadium',
       'Rajiv Gandhi International Stadium', 'MA Chidambaram Stadium',
       'Arun Jaitley Stadium', 'MA Chidambaram Stadium, Chepauk, Chennai',
       'Wankhede Stadium, Mumbai', 'Narendra Modi Stadium, Ahmedabad',
       'Arun Jaitley Stadium, Delhi', 'Zayed Cricket Stadium, Abu Dhabi',
       'Dr DY Patil Sports Academy, Mumbai',
       'Maharashtra Cricket Association Stadium, Pune',
       'Eden Gardens, Kolkata',
       'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
       'Rajiv Gandhi International Stadium, Uppal, Hyderabad',
       'M Chinnaswamy Stadium, Bengaluru',
       'Barsapara Cricket Stadium, Guwahati',
       'Sawai Mansingh Stadium, Jaipur',
       'Himachal Pradesh Cricket Association Stadium, Dharamsala']


def ipl():
    st.sidebar.title("IPL Analysis Dashboard")
    st.sidebar.image("https://th.bing.com/th/id/OIP.7qif-W3gYRPl-bnwJl3ygwHaHa?rs=1&pid=ImgDetMain")
    options = st.sidebar.selectbox("Choose an option", ["Home", "Batsman Analysis", "Bowler Analysis", "Venue Analysis", "Visualization"])

    if options == "Home":
        st.header("Welcome to IPL Analysis Dashboard")
        st.image("https://th.bing.com/th/id/R.d226e8ccd15ba748c3f33b93988a61b2?rik=PpT1Wm0dt%2fJozQ&riu=http%3a%2f%2fwww.aajkikhabar.com%2fen%2fwp-content%2fuploads%2f2019%2f02%2fIPL-Tournament-1-1.jpg&ehk=oANTwedvnkacVHJP8fauvjcyOrcbROWzTSF5FP01O0w%3d&risl=&pid=ImgRaw&r=0", use_column_width=True)
        # Introduction
        st.write("This dashboard provides analysis and insights into IPL cricket data from 2008 to 2023.")
        st.subheader("Key Features")
        st.write("- Batsman Analysis: Analyze batting performance of IPL players.")
        st.write("- Bowler Analysis: Explore bowling statistics and performance.")
        st.write("- Venue Analysis: Understand the impact of different venues on match outcomes.")
        st.subheader("Data Sources")
        st.write("The data used in this dashboard is sourced from Kaggle:")
        st.write("- deliveries.csv")
        st.write("- matches.csv")

        # Add any home page content here

    elif options == "Batsman Analysis":
        st.header("Batsman Analysis")
    
    # Dropdown for batsman and bowler selection
        selected_batsman = st.selectbox("Select Batsman", batsman)
        selected_bowler = st.selectbox("Select Bowler", bowler)
    
    # Batsman statistics
        st.subheader(selected_batsman)
        st.write("Batsman Strike Rate:", functionfile.strike_rate(selected_batsman))
        st.write("Batsman Average Runs Scored:", functionfile.avg_of_batsman(selected_batsman))
        st.write("Total Runs Scored:", functionfile.batsman_score(selected_batsman))
        st.write("Total Sixes:", functionfile.batsman_six(selected_batsman))
        st.write("Total Fours:", functionfile.batsman_four(selected_batsman))
    
    # Batsman performance against specific bowler
        st.write("Performance Against Specific Bowler")
        asb = functionfile.batsman_against_bowler(selected_batsman, selected_bowler)
        runs_against_bowler = asb['Runs']
        wickets_against_bowler = asb['Wicket']
        st.write(f"{selected_batsman} scored {runs_against_bowler} runs against {selected_bowler} and got out {wickets_against_bowler} times.")
    
    # Graph for batsman performance
        st.subheader(f"Performance Overview of {selected_batsman}")
        performance_data = figurs.batsman_performance_visualization(selected_batsman)  # Retrieve DataFrame and Plotly figure
        performance_df = performance_data['df']  # Batsman's performance DataFrame
        performance_fig = performance_data['fig']  # Visualization as a Plotly figure
    
        st.dataframe(performance_df)  # Display raw data
        st.plotly_chart(performance_fig)  # Interactive Plotly chart



    elif options == "Bowler Analysis":
        st.header("Bowler Analysis")
        selected_bowler = st.selectbox("Select Bowler", bowler)
        selected_players= st.selectbox('Select Death Player',death_players)
        st.subheader( selected_bowler)
        st.write("Death Wickets:", functionfile.death_wickets(selected_bowler))
        st.write("Death Wickets:", functionfile.death_wickets(selected_bowler))
        st.write("Total Wickets:", functionfile.bowler_wicket(selected_bowler))
        st.write("Bowling Average:", functionfile.bowling_avg(selected_bowler))
        st.write("Death Wickets:", functionfile.death_wickets(selected_bowler))
        st.write("Death Strike Rate:", functionfile.death_strike_rate(selected_players))
        # Add more analysis for bowler


    elif options == "Venue Analysis":
        st.header("Venue Related Analysis")
        selected_batsman = st.selectbox("Select Batsman", batsman)
        selected_venue = st.selectbox("Select Venue", venue)
        st.subheader(selected_venue)
        batting_stats = functionfile.batting_stats_in_venue(selected_batsman, selected_venue)

        st.write("Winning percentage of teams playing at a particular venue", functionfile.winning_percentage(selected_venue))
        st.write("Average total score at each venue",functionfile.average_score(selected_venue))
        st.write("Bowling performance at each venue",functionfile.bowling_performance(selected_venue))
        st.write("Winning the toss at different venues", functionfile.toss_analysis(selected_venue))
        st.write("Batting Stats for", selected_batsman, "at", selected_venue)
        st.write("Total Runs:", batting_stats['Total Runs'])
        st.write("Total Balls:", batting_stats['Total Balls'])
        st.write("Strike Rate:", batting_stats['Strike Rate'])
        st.write("## Venue that hosted the maximum number of matches")
        x1=functionfile.venue_with_max_matches()
        st.plotly_chart(x1)


    elif options =="Visualization":
        st.header("Visual graphs")
        st.write('### Season Wise IPL Matches')
        d1=functionfile.matches_per_season_visualization()
        st.plotly_chart(d1)
        st.write("### IPL Matches Played by Each Team")
        d2= functionfile.plot_matches_per_team()
        st.plotly_chart(d2)
        st.write("### Most IPL Runs by a Batsman")
        d3=functionfile.most_runs_by_batsman()
        st.plotly_chart(d3)
        st.write("### Umpire with most IPL matches")
        top_umpire = functionfile.umpire_with_most_matches()
        # Display the top umpire
        top_umpire_data = top_umpire['data'][0]['y'][0]  
        top_umpire_name = top_umpire['data'][0]['y'][0]
        st.write(f"The umpire with the most IPL matches is {top_umpire_name} with {top_umpire_data} matches.")
        # Display the plot in Streamlit
        st.plotly_chart(top_umpire)

