# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2014 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""
Indian districts and staes maps

"""

from __future__ import division
from collections import defaultdict
from pygal.graph.map import BaseMap
from pygal._compat import u
from numbers import Number
import os

'''
https://en.wikipedia.org/wiki/List_of_districts_in_India 
'''

DISTRICTS = {
    'AN-NI': u("Nicobar"),
    'AN-NA': u("North and Middle Andaman"),
    'AN-SA': u("South Andaman"),
    'AP-AN': u("Anantapur"),
    'AP-CH': u("Chittoor"),
    'AP-EG': u("East Godavari"),
    'AP-GU': u("Guntur"),
    'AP-CU': u("Kadapa"),
    'AP-KR': u("Krishna"),
    'AP-KU': u("Kurnool"),
    'AP-PR': u("Prakasam"),
    'AP-NE': u("Nellore"),
    'AP-SR': u("Srikakulam"),
    'AP-VS': u("Visakhapatnam"),
    'AP-VZ': u("Vizianagaram"),
    'AP-WG': u("West Godavari"),
    'AR-AJ': u("Anjaw"),
    'AR-CH': u("Changlang"),
    'AR-UD': u("Dibang Valley"),
    'AR-EK': u("East Kameng"),
    'AR-ES': u("East Siang"),
    'AR-KK': u("Kurung Kumey"),
    'AR-EL': u("Lohit"),
    'AR-LD': u("Longding"),
    'AR-DV': u("Lower Dibang Valley"),
    'AR-LB': u("Lower Subansiri"),
    'AR-PA': u("Papum Pare"),
    'AR-TA': u("Tawang"),
    'AR-TI': u("Tirap"),
    'AR-US': u("Upper Siang"),
    'AR-UB': u("Upper Subansiri"),
    'AR-WK': u("West Kameng"),
    'AR-WS': u("West Siang"),
    'AS-BK': u("Baksa"),
    'AS-BP': u("Barpeta"),
    'AS-BS': u("Bishwanath"),
    'AS-BO': u("Bongaigaon"),
    'AS-CA': u("Cachar"),
    'AS-CD': u("Charaideo"),
    'AS-CH': u("Chirang"),
    'AS-DR': u("Darrang"),
    'AS-DM': u("Dhemaji"),
    'AS-DU': u("Dhubri"),
    'AS-DI': u("Dibrugarh"),
    'AS-NC': u("Dima Hasao"),
    'AS-GP': u("Goalpara"),
    'AS-GG': u("Golaghat"),
    'AS-HA': u("Hailakandi"),
    'AS-HJ': u("Hojai"),
    'AS-JO': u("Jorhat"),
    'AS-KU': u("Kamrup"),
    'AS-KM': u("Kamrup Metropolitan"),
    'AS-KG': u("Karbi Anglong"),
    'AS-KR': u("Karimganj"),
    'AS-KJ': u("Kokrajhar"),
    'AS-LA': u("Lakhimpur"),
    'AS-MJ': u("Majuli"),
    'AS-MA': u("Morigaon"),
    'AS-NN': u("Nagaon"),
    'AS-NB': u("Nalbari"),
    'AS-ST': u("Sivasagar"),
    'AS-SM': u("South Salmara-Mankachar"),
    'AS-SO': u("Sonitpur"),
    'AS-TI': u("Tinsukia"),
    'AS-UD': u("Udalguri"),
    'AS-WK': u("West Karbi Anglong"),
    'BR-AR': u("Araria"),
    'BR-AR': u("Arwal"),
    'BR-AU': u("Aurangabad"),
    'BR-BA': u("Banka"),
    'BR-BE': u("Begusarai"),
    'BR-BG': u("Bhagalpur"),
    'BR-BJ': u("Bhojpur"),
    'BR-BU': u("Buxar"),
    'BR-DA': u("Darbhanga"),
    'BR-EC': u("East Champaran"),
    'BR-GA': u("Gaya"),
    'BR-GO': u("Gopalganj"),
    'BR-JA': u("Jamui"),
    'BR-JE': u("Jehanabad"),
    'BR-KM': u("Kaimur"),
    'BR-KT': u("Katihar"),
    'BR-KH': u("Khagaria"),
    'BR-KI': u("Kishanganj"),
    'BR-LA': u("Lakhisarai"),
    'BR-MP': u("Madhepura"),
    'BR-MB': u("Madhubani"),
    'BR-MG': u("Munger"),
    'BR-MZ': u("Muzaffarpur"),
    'BR-NL': u("Nalanda"),
    'BR-NW': u("Nawada"),
    'BR-PA': u("Patna"),
    'BR-PU': u("Purnia"),
    'BR-RO': u("Rohtas"),
    'BR-SH': u("Saharsa"),
    'BR-SM': u("Samastipur"),
    'BR-SR': u("Saran"),
    'BR-SP': u("Sheikhpura"),
    'BR-SO': u("Sheohar"),
    'BR-ST': u("Sitamarhi"),
    'BR-SW': u("Siwan"),
    'BR-SU': u("Supaul"),
    'BR-VA': u("Vaishali"),
    'BR-WC': u("West Champaran"),
    'CH-CH': u("Chandigarh"),
    'CG-BA': u("Bastar"),
    'CG-BJ': u("Bijapur"),
    'CG-BI': u("Bilaspur"),
    'CG-DA': u("Dantewada"),
    'CG-DH': u("Dhamtari"),
    'CG-DU': u("Durg"),
    'CG-JC': u("Janjgir-Champa"),
    'CG-JA': u("Jashpur"),
    'CG-KW': u("Kawardha"),
    'CG-KK': u("Kanker"),
    'CG-KB': u("Korba"),
    'CG-KJ': u("Koriya"),
    'CG-MA': u("Mahasamund"),
    'CG-NR': u("Narayanpur"),
    'CG-RG': u("Raigarh"),
    'CG-RP': u("Raipur"),
    'CG-RN': u("Rajnandgaon"),
    'CG-SK': u("Sukma"),
    'CG-SJ': u("Surajpur"),
    'CG-SJ': u("Surguja"),
    'DN-DN': u("Dadra and Nagar Haveli"),
    'DD-DA': u("Daman"),
    'DD-DI': u("Diu"),
    'DL-CD': u("Central Delhi"),
    'DL-ED': u("East Delhi"),
    'DL-ND': u("New Delhi"),
    'DL-NO': u("North Delhi"),
    'DL-NE': u("North East Delhi"),
    'DL-NW': u("North West Delhi"),
    'DL-SD': u("South Delhi"),
    'DL-SW': u("South West Delhi"),
    'DL-WD': u("West Delhi"),
    'GA-NG': u("North Goa"),
    'GA-SG': u("South Goa"),
    'GJ-AH': u("Ahmedabad"),
    'GJ-AM': u("Amreli"),
    'GJ-AN': u("Anand"),
    'GJ-AR': u("Aravalli"),
    'GJ-BK': u("Banaskantha"),
    'GJ-BR': u("Bharuch"),
    'GJ-BV': u("Bhavnagar"),
    'GJ-DA': u("Dahod"),
    'GJ-DG': u("Dang"),
    'GJ-GA': u("Gandhinagar"),
    'GJ-JA': u("Jamnagar"),
    'GJ-JU': u("Junagadh"),
    'GJ-KH': u("Kheda"),
    'GJ-KA': u("Kutch"),
    'GJ-MH': u("Mahisagar"),
    'GJ-MA': u("Mehsana"),
    'GJ-NR': u("Narmada"),
    'GJ-NV': u("Navsari"),
    'GJ-PM': u("Panchmahal"),
    'GJ-PA': u("Patan"),
    'GJ-PO': u("Porbandar"),
    'GJ-RA': u("Rajkot"),
    'GJ-SK': u("Sabarkantha"),
    'GJ-ST': u("Surat"),
    'GJ-SN': u("Surendranagar"),
    'GJ-TA': u("Tapi"),
    'GJ-VD': u("Vadodara"),
    'GJ-VL': u("Valsad"),
    'HR-AM': u("Ambala"),
    'HR-BH': u("Bhiwani"),
    'HR-FR': u("Faridabad"),
    'HR-FT': u("Fatehabad"),
    'HR-GU': u("Gurgaon"),
    'HR-HI': u("Hissar"),
    'HR-JH': u("Jhajjar"),
    'HR-JI': u("Jind"),
    'HR-KT': u("Kaithal"),
    'HR-KR': u("Karnal"),
    'HR-KU': u("Kurukshetra"),
    'HR-MA': u("Mahendragarh"),
    'HR-MW': u("Nuh"),
    'HR-PW': u("Palwal"),
    'HR-PK': u("Panchkula"),
    'HR-PP': u("Panipat"),
    'HR-RE': u("Rewari"),
    'HR-RO': u("Rohtak"),
    'HR-SI': u("Sirsa"),
    'HR-SNP': u("Sonipat"),
    'HR-YN': u("Yamuna Nagar"),
    'HP-BI': u("Bilaspur"),
    'HP-CH': u("Chamba"),
    'HP-HA': u("Hamirpur"),
    'HP-KA': u("Kangra"),
    'HP-KI': u("Kinnaur"),
    'HP-KU': u("Kullu"),
    'HP-LS': u("Lahaul and Spiti"),
    'HP-MA': u("Mandi"),
    'HP-SH': u("Shimla"),
    'HP-SI': u("Sirmaur"),
    'HP-SO': u("Solan"),
    'HP-UNA': u("Una"),
    'JK-AN': u("Anantnag"),
    'JK-BPR': u("Bandipora"),
    'JK-BR': u("Baramulla"),
    'JK-BD': u("Badgam"),
    'JK-DO': u("Doda"),
    'JK-GB': u("Ganderbal"),
    'JK-JA': u("Jammu"),
    'JK-KR': u("Kargil"),
    'JK-KT': u("Kathua"),
    'JK-KW': u("Kishtwar"),
    'JK-KG': u("Kulgam"),
    'JK-KU': u("Kupwara"),
    'JK-LE': u("Leh"),
    'JK-PO': u("Poonch"),
    'JK-PU': u("Pulwama"),
    'JK-RA': u("Rajouri"),
    'JK-RB': u("Ramban"),
    'JK-RS': u("Reasi"),
    'JK-SB': u("Samba"),
    'JK-SH': u("Shopian"),
    'JK-SR': u("Srinagar"),
    'JK-UD': u("Udhampur"),
    'JH-BO': u("Bokaro"),
    'JH-CH': u("Chatra"),
    'JH-DE': u("Deoghar"),
    'JH-DH': u("Dhanbad"),
    'JH-DU': u("Dumka"),
    'JH-ES': u("East Singhbhum"),
    'JH-GA': u("Garhwa"),
    'JH-GI': u("Giridih"),
    'JH-GO': u("Godda"),
    'JH-GU': u("Gumla"),
    'JH-HA': u("Hazaribag"),
    'JH-JA': u("Jamtara"),
    'JH-KH': u("Khunti"),
    'JH-KO': u("Koderma"),
    'JH-LA': u("Latehar"),
    'JH-LO': u("Lohardaga"),
    'JH-PK': u("Pakur"),
    'JH-PL': u("Palamu"),
    'JH-RM': u("Ramgarh"),
    'JH-RA': u("Ranchi"),
    'JH-SA': u("Sahibganj"),
    'JH-SK': u("Seraikela Kharsawan"),
    'JH-SI': u("Simdega"),
    'JH-WS': u("West Singhbhum"),
    'KA-BK': u("Bagalkot"),
    'KA-BL': u("Ballari"),
    'KA-BG': u("Belagavi"),
    'KA-BR': u("Bengaluru Rural"),
    'KA-BN': u("Bengaluru Urban"),
    'KA-BD': u("Bidar"),
    'KA-CJ': u("Chamarajnagar"),
    'KA-CK': u("Chikkaballapur"),
    'KA-CK': u("Chikkamagaluru"),
    'KA-CT': u("Chitradurga"),
    'KA-DK': u("Dakshina Kannada"),
    'KA-DA': u("Davanagere"),
    'KA-DH': u("Dharwad"),
    'KA-GA': u("Gadag"),
    'KA-HS': u("Hassan"),
    'KA-HV': u("Haveri"),
    'KA-GU': u("Kalaburagi"),
    'KA-KD': u("Kodagu"),
    'KA-KL': u("Kolar"),
    'KA-KP': u("Koppal"),
    'KA-MA': u("Mandya"),
    'KA-MY': u("Mysuru"),
    'KA-RA': u("Raichur"),
    'KA-RM': u("Ramanagara"),
    'KA-SH': u("Shivamogga"),
    'KA-TU': u("Tumakuru"),
    'KA-UD': u("Udupi"),
    'KA-UK': u("Uttara Kannada"),
    'KA-BJ': u("Vijayapura"),
    'KA-YG': u("Yadgir"),
    'KL-AL': u("Alappuzha"),
    'KL-ER': u("Ernakulam"),
    'KL-ID': u("Idukki"),
    'KL-KN': u("Kannur"),
    'KL-KS': u("Kasaragod"),
    'KL-KL': u("Kollam"),
    'KL-KT': u("Kottayam"),
    'KL-KZ': u("Kozhikode"),
    'KL-MA': u("Malappuram"),
    'KL-PL': u("Palakkad"),
    'KL-PT': u("Pathanamthitta"),
    'KL-TS': u("Thrissur"),
    'KL-TV': u("Thiruvananthapuram"),
    'KL-WA': u("Wayanad"),
    'LD-LD': u("Lakshadweep"),
    'MP-AG': u("Agar Malwa"),
    'MP-AL': u("Alirajpur"),
    'MP-AP': u("Anuppur"),
    'MP-AS': u("Ashok Nagar"),
    'MP-BL': u("Balaghat"),
    'MP-BR': u("Barwani"),
    'MP-BE': u("Betul"),
    'MP-BD': u("Bhind"),
    'MP-BP': u("Bhopal"),
    'MP-BU': u("Burhanpur"),
    'MP-CT': u("Chhatarpur"),
    'MP-CN': u("Chhindwara"),
    'MP-DM': u("Damoh"),
    'MP-DT': u("Datia"),
    'MP-DE': u("Dewas"),
    'MP-DH': u("Dhar"),
    'MP-DI': u("Dindori"),
    'MP-GU': u("Guna"),
    'MP-GW': u("Gwalior"),
    'MP-HA': u("Harda"),
    'MP-HO': u("Hoshangabad"),
    'MP-IN': u("Indore"),
    'MP-JA': u("Jabalpur"),
    'MP-JH': u("Jhabua"),
    'MP-KA': u("Katni"),
    'MP-EN': u("East Nimar"),
    'MP-WN': u("West Nimar"),
    'MP-ML': u("Mandla"),
    'MP-MS': u("Mandsaur"),
    'MP-MO': u("Morena"),
    'MP-NA': u("Narsinghpur"),
    'MP-NE': u("Neemuch"),
    'MP-PA': u("Panna"),
    'MP-RS': u("Raisen"),
    'MP-RG': u("Rajgarh"),
    'MP-RL': u("Ratlam"),
    'MP-RE': u("Rewa"),
    'MP-SG': u("Sagar"),
    'MP-ST': u("Satna"),
    'MP-SR': u("Sehore"),
    'MP-SO': u("Seoni"),
    'MP-SH': u("Shahdol"),
    'MP-SJ': u("Shajapur"),
    'MP-SP': u("Sheopur"),
    'MP-SV': u("Shivpuri"),
    'MP-SI': u("Sidhi"),
    'MP-SN': u("Singrauli"),
    'MP-TI': u("Tikamgarh"),
    'MP-UJ': u("Ujjain"),
    'MP-UM': u("Umaria"),
    'MP-VI': u("Vidisha"),
    'MH-AH': u("Ahmednagar"), #Maharashtra
    'MH-AK': u("Akola"),
    'MH-AM': u("Amravati"),
    'MH-AU': u("Aurangabad"),
    'MH-BI': u("Beed"),
    'MH-BH': u("Bhandara"),
    'MH-BU': u("Buldhana"),
    'MH-CH': u("Chandrapur"),
    'MH-DH': u("Dhule"),
    'MH-GA': u("Gadchiroli"),
    'MH-GO': u("Gondia"),
    'MH-HI': u("Hingoli"),
    'MH-JG': u("Jalgaon"),
    'MH-JN': u("Jalna"),
    'MH-KO': u("Kolhapur"),
    'MH-LA': u("Latur"),
    'MH-MC': u("Mumbai City"),
    'MH-MU': u("Mumbai suburban"),
    'MH-ND': u("Nanded"),
    'MH-NB': u("Nandurbar"),
    'MH-NG': u("Nagpur"),
    'MH-NS': u("Nashik"),
    'MH-OS': u("Osmanabad"),
    'MH-PL': u("Palghar"),
    'MH-PA': u("Parbhani"),
    'MH-PU': u("Pune"),
    'MH-RG': u("Raigad"),
    'MH-RT': u("Ratnagiri"),
    'MH-SN': u("Sangli"),
    'MH-ST': u("Satara"),
    'MH-SI': u("Sindhudurg"),
    'MH-SO': u("Solapur"),
    'MH-TH': u("Thane"),
    'MH-WR': u("Wardha"),
    'MH-WS': u("Washim"),
    'MH-YA': u("Yavatmal"),
    'MN-BI': u("Bishnupur"),
    'MN-CC': u("Churachandpur"),
    'MN-CD': u("Chandel"),
    'MN-EI': u("Imphal East"),
    'MN-SE': u("Senapati"),
    'MN-TA': u("Tamenglong"),
    'MN-TH': u("Thoubal"),
    'MN-UK': u("Ukhrul"),
    'MN-WI': u("Imphal West"),
    'ML-EG': u("East Garo Hills"),
    'ML-EK': u("East Khasi Hills"),
    'ML-RB': u("Ri Bhoi"),
    'ML-SG': u("South Garo Hills"),
    'ML-WG': u("West Jaintia Hills"),
    'ML-WG': u("West Garo Hills"),
    'ML-WK': u("West Khasi Hills"),
    'MZ-AI': u("Aizawl"),
    'MZ-CH': u("Champhai"),
    'MZ-KO': u("Kolasib"),
    'MZ-LA': u("Lawngtlai"),
    'MZ-LU': u("Lunglei"),
    'MZ-MA': u("Mamit"),
    'MZ-SA': u("Saiha"),
    'MZ-SE': u("Serchhip"),
    'NL-DI': u("Dimapur"),
    'NL-KI': u("Kiphire"),
    'NL-KO': u("Kohima"),
    'NL-LO': u("Longleng"),
    'NL-MK': u("Mokokchung"),
    'NL-MN': u("Mon"),
    'NL-PE': u("Peren"),
    'NL-PH': u("Phek"),
    'NL-TU': u("Tuensang"),
    'NL-WO': u("Wokha"),
    'NL-ZU': u("Zunheboto"),
    'OD-AN': u("Angul"),
    'OD-BD': u("Boudh"),
    'OD-BH': u("Bhadrak"),
    'OD-BL': u("Balangir"),
    'OD-BR': u("Bargarh"),
    'OD-BW': u("Balasore"),
    'OD-CU': u("Cuttack"),
    'OD-DE': u("Debagarh"),
    'OD-DH': u("Dhenkanal"),
    'OD-GN': u("Ganjam"),
    'OD-GP': u("Gajapati"),
    'OD-JH': u("Jharsuguda"),
    'OD-JP': u("Jajpur"),
    'OD-JS': u("Jagatsinghpur"),
    'OD-KH': u("Khordha"),
    'OD-KJ': u("Kendujhar"),
    'OD-KL': u("Kalahandi"),
    'OD-KN': u("Kandhamal"),
    'OD-KO': u("Koraput"),
    'OD-KP': u("Kendrapara"),
    'OD-ML': u("Malkangiri"),
    'OD-MY': u("Mayurbhanj"),
    'OD-NB': u("Nabarangpur"),
    'OD-NU': u("Nuapada"),
    'OD-NY': u("Nayagarh"),
    'OD-PU': u("Puri"),
    'OD-RA': u("Rayagada"),
    'OD-SA': u("Sambalpur"),
    'OD-SO': u("Sonepur"),
    'OD-SU': u("Sundargarh"),
    'PY-KA': u("Karaikal"),
    'PY-MA': u("Mahe"),
    'PY-PO': u("Pondicherry"),
    'PY-YA': u("Yanam"),
    'PB-AM': u("Amritsar"),
    'PB-BNL': u("Barnala"),
    'PB-BA': u("Bathinda"),
    'PB-FI': u("Firozpur"),
    'PB-FR': u("Faridkot"),
    'PB-FT': u("Fatehgarh Sahib"),
    'PB-FA': u("Fazilka"),
    'PB-GU': u("Gurdaspur"),
    'PB-HO': u("Hoshiarpur"),
    'PB-JA': u("Jalandhar"),
    'PB-KA': u("Kapurthala"),
    'PB-LU': u("Ludhiana"),
    'PB-MA': u("Mansa"),
    'PB-MO': u("Moga"),
    'PB-MU': u("Sri Muktsar Sahib"),
    'PB-PA': u("Pathankot"),
    'PB-PA': u("Patiala"),
    'PB-RU': u("Rupnagar"),
    'PB-SAS': u("Sahibzada Ajit Singh Nagar"),
    'PB-SA': u("Sangrur"),
    'PB-PB': u("Shahid Bhagat Singh Nagar"),
    'PB-TT': u("Tarn Taran"),
    'RJ-AJ': u("Ajmer"),
    'RJ-AL': u("Alwar"),
    'RJ-BI': u("Bikaner"),
    'RJ-BM': u("Barmer"),
    'RJ-BN': u("Banswara"),
    'RJ-BP': u("Bharatpur"),
    'RJ-BR': u("Baran"),
    'RJ-BU': u("Bundi"),
    'RJ-BW': u("Bhilwara"),
    'RJ-CR': u("Churu"),
    'RJ-CT': u("Chittorgarh"),
    'RJ-DA': u("Dausa"),
    'RJ-DH': u("Dholpur"),
    'RJ-DU': u("Dungarpur"),
    'RJ-GA': u("Ganganagar"),
    'RJ-HA': u("Hanumangarh"),
    'RJ-JJ': u("Jhunjhunu"),
    'RJ-JL': u("Jalore"),
    'RJ-JO': u("Jodhpur"),
    'RJ-JP': u("Jaipur"),
    'RJ-JS': u("Jaisalmer"),
    'RJ-JW': u("Jhalawar"),
    'RJ-KA': u("Karauli"),
    'RJ-KO': u("Kota"),
    'RJ-NA': u("Nagaur"),
    'RJ-PA': u("Pali"),
    'RJ-PG': u("Pratapgarh"),
    'RJ-RA': u("Rajsamand"),
    'RJ-SK': u("Sikar"),
    'RJ-SM': u("Sawai Madhopur"),
    'RJ-SR': u("Sirohi"),
    'RJ-TO': u("Tonk"),
    'RJ-UD': u("Udaipur"),
    'SK-ES': u("East Sikkim"),
    'SK-NS': u("North Sikkim"),
    'SK-SS': u("South Sikkim"),
    'SK-WS': u("West Sikkim"),
    'TN-AY': u("Ariyalur"),
    'TN-CH': u("Chennai"),
    'TN-CO': u("Coimbatore"),
    'TN-CU': u("Cuddalore"),
    'TN-DH': u("Dharmapuri"),
    'TN-DI': u("Dindigul"),
    'TN-ER': u("Erode"),
    'TN-KC': u("Kanchipuram"),
    'TN-KK': u("Kanyakumari"),
    'TN-KA': u("Karur"),
    'TN-KR': u("Krishnagiri"),
    'TN-MA': u("Madurai"),
    'TN-NG': u("Nagapattinam"),
    'TN-NI': u("Nilgiris"),
    'TN-NM': u("Namakkal"),
    'TN-PE': u("Perambalur"),
    'TN-PU': u("Pudukkottai"),
    'TN-RA': u("Ramanathapuram"),
    'TN-SA': u("Salem"),
    'TN-SI': u("Sivaganga"),
    'TN-TP': u("Tirupur"),
    'TN-TC': u("Tiruchirappalli"),
    'TN-TH': u("Theni"),
    'TN-TI': u("Tirunelveli"),
    'TN-TJ': u("Thanjavur"),
    'TN-TK': u("Thoothukudi"),
    'TN-TL': u("Tiruvallur"),
    'TN-TR': u("Tiruvarur"),
    'TN-TV': u("Tiruvannamalai"),
    'TN-VE': u("Vellore"),
    'TN-VL': u("Viluppuram"),
    'TN-VR': u("Virudhunagar"),
    'TS-AD': u("Adilabad"),
    'TS-HY': u("Hyderabad"),
    'TS-KA': u("Karimnagar"),
    'TS-KH': u("Khammam"),
    'TS-MA': u("Mahbubnagar"),
    'TS-ME': u("Medak"),
    'TS-NA': u("Nalgonda"),
    'TS-NI': u("Nizamabad"),
    'TS-RA': u("Ranga Reddy"),
    'TS-WL': u("Warangal "),
    'TR-DH': u("Dhalai"),
    'TR-GM': u("Gomati"),
    'TR-KH': u("Khowai"),
    'TR-NT': u("North Tripura"),
    'TR-SP': u("Sepahijala"),
    'TR-ST': u("South Tripura"),
    'TR-UK': u("Unokoti"),
    'TR-WT': u("West Tripura"),
    'UP-AG': u("Agra"),
    'UP-AL': u("Aligarh"),
    'UP-AH': u("Allahabad"),
    'UP-AN': u("Ambedkar Nagar"),
    'UP-CS': u("Chhatrapati Shahuji Maharaj Nagar"),
    'UP-JP': u("Jyotiba Phule Nagar"),
    'UP-AU': u("Auraiya"),
    'UP-AZ': u("Azamgarh"),
    'UP-BG': u("Bagpat"),
    'UP-BH': u("Bahraich"),
    'UP-BL': u("Ballia"),
    'UP-BP': u("Balrampur"),
    'UP-BN': u("Banda"),
    'UP-BB': u("Barabanki"),
    'UP-BR': u("Bareilly"),
    'UP-BS': u("Basti"),
    'UP-BI': u("Bijnor"),
    'UP-BD': u("Budaun"),
    'UP-BU': u("Bulandshahr"),
    'UP-CD': u("Chandauli"),
    'UP-CT': u("Chitrakoot"),
    'UP-DE': u("Deoria"),
    'UP-ET': u("Etah"),
    'UP-EW': u("Etawah"),
    'UP-FZ': u("Faizabad"),
    'UP-FR': u("Farrukhabad"),
    'UP-FT': u("Fatehpur"),
    'UP-FI': u("Firozabad"),
    'UP-GB': u("Gautam Buddh Nagar"),
    'UP-GZ': u("Ghaziabad"),
    'UP-GP': u("Ghazipur"),
    'UP-GN': u("Gonda"),
    'UP-GR': u("Gorakhpur"),
    'UP-HM': u("Hamirpur"),
    'UP-PN': u("Panchsheel Nagar"),
    'UP-HR': u("Hardoi"),
    'UP-HT': u("Hathras"),
    'UP-JL': u("Jalaun"),
    'UP-JU': u("Jaunpur"),
    'UP-JH': u("Jhansi"),
    'UP-KJ': u("Kannauj"),
    'UP-KD': u("Kanpur Dehat"),
    'UP-KN': u("Kanpur Nagar"),
    'UP-KR': u("Kanshi Ram Nagar"),
    'UP-KS': u("Kaushambi"),
    'UP-KU': u("Kushinagar"),
    'UP-LK': u("Lakhimpur Kheri"),
    'UP-LA': u("Lalitpur"),
    'UP-LU': u("Lucknow"),
    'UP-MG': u("Maharajganj"),
    'UP-MH': u("Mahoba"),
    'UP-MP': u("Mainpuri"),
    'UP-MT': u("Mathura"),
    'UP-MB': u("Mau"),
    'UP-ME': u("Meerut"),
    'UP-MI': u("Mirzapur"),
    'UP-MO': u("Moradabad"),
    'UP-MU': u("Muzaffarnagar"),
    'UP-PI': u("Pilibhit"),
    'UP-PR': u("Pratapgarh"),
    'UP-RB': u("Raebareli"),
    'UP-RA': u("Rampur"),
    'UP-SA': u("Saharanpur"),
    'UP-SM': u("Sambhal"),
    'UP-SK': u("Sant Kabir Nagar"),
    'UP-SR': u("Bhadohi"),
    'UP-SJ': u("Shahjahanpur"),
    'UP-SH': u("Shamli"),
    'UP-SV': u("Shravasti"),
    'UP-SN': u("Siddharthnagar"),
    'UP-SI': u("Sitapur"),
    'UP-SO': u("Sonbhadra"),
    'UP-SU': u("Sultanpur"),
    'UP-UN': u("Unnao"),
    'UP-VA': u("Varanasi"),
    'UK-AL': u("Almora"),
    'UK-BA': u("Bageshwar"),
    'UK-CL': u("Chamoli"),
    'UK-CP': u("Champawat"),
    'UK-DD': u("Dehradun"),
    'UK-HA': u("Haridwar"),
    'UK-NA': u("Nainital"),
    'UK-PG': u("Pauri Garhwal"),
    'UK-PI': u("Pithoragarh"),
    'UK-RP': u("Rudraprayag"),
    'UK-TG': u("Tehri Garhwal"),
    'UK-US': u("Udham Singh Nagar"),
    'UK-UT': u("Uttarkashi"),
    'WB-AD': u("Alipurduar"),
    'WB-BN': u("Bankura"),
    'WB-BR': u("Bardhaman"),
    'WB-BI': u("Birbhum"),
    'WB-KB': u("Cooch Behar"),
    'WB-DD': u("Dakshin Dinajpur"),
    'WB-DA': u("Darjeeling"),
    'WB-HG': u("Hooghly"),
    'WB-HR': u("Howrah"),
    'WB-JA': u("Jalpaiguri"),
    'WB-JH': u("Jhargram"),
    'WB-KA': u("Kalimpong"),
    'WB-KO': u("Kolkata"),
    'WB-MA': u("Maldah"),
    'WB-MSD': u("Murshidabad"),
    'WB-NA': u("Nadia"),
    'WB-PN': u("North 24 Parganas"),
    'WB-PM': u("Paschim Medinipur"),
    'WB-PR': u("Purba Medinipur"),
    'WB-PU': u("Purulia"),
    'WB-PS': u("South 24 Parganas"),
    'WB-UD': u("Uttar Dinajpur"),
     
}


STATES = {
    'AP': u("Andhra Pradesh"),
    'AR': u("Arunachal Pradesh"),
    'AS': u("Assam"),
    'BR': u("Bihar"),
    'CG': u("Chhattisgarh"),
    'GA': u("Goa"),
    'GJ': u("Gujarat"),
    'HR': u("Haryana"),
    'HP': u("Himachal Pradesh"),
    'JK': u("Jammu and Kashmir"),
    'JH': u("Jharkhand"),
    'KA': u("Karnataka"),
    'KL': u("Kerala"),
    'MP': u("Madhya Pradesh"),
    'MH': u("Maharashtra"),
    'MN': u("Manipur"),
    'ML': u("Meghalaya"),
    'MZ': u("Mizoram"),
    'NL': u("Nagaland"),
    'OD': u("Odisha"),
    'PB': u("Punjab"),
    'RJ': u("Rajasthan"),
    'SK': u("Sikkim"),
    'TN': u("Tamil Nadu"),
    'TS': u("Telangana"),
    'TR': u("Tripura"),
    'UP': u("Uttar Pradesh"),
    'UK': u("Uttarakhand"),
    'WB': u("West Bengal"),
    'AN': u("Andaman and Nicobar"),
    'CH': u("Chandigarh"),
    'DN': u("Dadra and Nagar Haveli"),
    'DD': u("Daman and Diu"),
    'LD': u("Lakshadweep"),
    'DL': u("Delhi"),
    'PY': u("Puducherry"),
}


with open(os.path.join(
        os.path.dirname(__file__),
        'in.districts.svg')) as file:
    DPT_MAP = file.read()


class IntCodeMixin(object):
    def adapt_code(self, area_code):
        if isinstance(area_code, Number):
            return '%02d' % area_code
        return super(IntCodeMixin, self).adapt_code(area_code)


class Districts(IntCodeMixin, BaseMap):
    """Indian Districts map"""
    x_labels = list(DISTRICTS.keys())
    area_names = DISTRICTS
    area_prefix = 'z'
    kind = 'district'
    svg_map = DPT_MAP


with open(os.path.join(
        os.path.dirname(__file__),
        'in.states.svg')) as file:
    REG_MAP = file.read()


class States(IntCodeMixin, BaseMap):
    """Indian States map"""
    x_labels = list(STATES.keys())
    area_names = STATES
    area_prefix = 'a'
    svg_map = REG_MAP
    kind = 'state'


DISTRICTS_STATES = {
    "01": "82",
    "02": "22",
    "03": "83",
    "04": "93",
    "05": "93",
    "06": "93",
    "07": "82",
    "08": "21",
    "09": "73",
    "10": "21",
    "11": "91",
    "12": "73",
    "13": "93",
    "14": "25",
    "15": "83",
    "16": "54",
    "17": "54",
    "18": "24",
    "19": "74",
    "21": "26",
    "22": "53",
    "23": "74",
    "24": "72",
    "25": "43",
    "26": "82",
    "27": "23",
    "28": "24",
    "29": "53",
    "2A": "94",
    "2B": "94",
    "30": "91",
    "31": "73",
    "32": "73",
    "33": "72",
    "34": "91",
    "35": "53",
    "36": "24",
    "37": "24",
    "38": "82",
    "39": "43",
    "40": "72",
    "41": "24",
    "42": "82",
    "43": "83",
    "44": "52",
    "45": "24",
    "46": "73",
    "47": "72",
    "48": "91",
    "49": "52",
    "50": "25",
    "51": "21",
    "52": "21",
    "53": "52",
    "54": "41",
    "55": "41",
    "56": "53",
    "57": "41",
    "58": "26",
    "59": "31",
    "60": "22",
    "61": "25",
    "62": "31",
    "63": "83",
    "64": "72",
    "65": "73",
    "66": "91",
    "67": "42",
    "68": "42",
    "69": "82",
    "70": "43",
    "71": "26",
    "72": "52",
    "73": "82",
    "74": "82",
    "75": "11",
    "76": "23",
    "77": "11",
    "78": "11",
    "79": "54",
    "80": "22",
    "81": "73",
    "82": "73",
    "83": "93",
    "84": "93",
    "85": "52",
    "86": "54",
    "87": "74",
    "88": "41",
    "89": "26",
    "90": "43",
    "91": "11",
    "92": "11",
    "93": "11",
    "94": "11",
    "95": "11",
    "971": "01",
    "972": "02",
    "973": "03",
    "974": "04",
    "975": "05",
    "976": "06"
}


def aggregate_states(values):
    if isinstance(values, dict):
        values = values.items()
    states = defaultdict(int)
    for district, value in values:
        states[DISTRICTS_STATES[district]] += value
    return list(states.items())
