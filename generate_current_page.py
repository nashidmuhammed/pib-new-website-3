import html
import json
import os

ASSET_PREFIX = "PIB%20Delhi,%20Press%20Information%20Bureau_files/"

# Load dataset
slides_data = [
    {
        "id": 1,
        "img": ASSET_PREFIX + "T202608107455_004_-0eu.avif",
        "caption": "PM joined group photos with the Commonwealth Games (CWG) - 2026 medal winning players at his residence, in New Delhi.",
        "date": "10 August 2026",
        "category": "Sports & Youth Affairs"
    },
    {
        "id": 2,
        "img": ASSET_PREFIX + "T202608087454_010_-0eu.avif",
        "caption": "PM attends the 57th Convocation Ceremony of IIT Delhi, in New Delhi",
        "date": "08 August 2026",
        "category": "Education & Research"
    },
    {
        "id": 3,
        "img": ASSET_PREFIX + "T202608017451_004_-0eu.avif",
        "caption": "PM at the inauguration of Swami Vivekananda Cultural Youth Center- Viveka Smaraka, Sri Ramakrishna Ashrama, at Mysuru, in Karnataka",
        "date": "01 August 2026",
        "category": "Culture & Heritage"
    },
    {
        "id": 4,
        "img": ASSET_PREFIX + "T202608017450_009_-0eu.avif",
        "caption": "PM pays floral tributes to Swami Vivekananda at Viveka Smaraka, Sri Ramakrishna Ashrama, Mysuru",
        "date": "01 August 2026",
        "category": "National Commemoration"
    },
    {
        "id": 5,
        "img": ASSET_PREFIX + "T202607207443_014_-0eu.avif",
        "caption": "PM addressing the media on the first day of Monsoon Session of Parliament at Parliament House Complex, in New Delhi.",
        "date": "20 July 2026",
        "category": "Parliamentary Affairs"
    },
    {
        "id": 6,
        "img": ASSET_PREFIX + "T202607177442_008_-0eu.avif",
        "caption": "PM addressing at the laying foundation stone and dedication to the nation various development projects, in Chandigarh",
        "date": "17 July 2026",
        "category": "National Infrastructure"
    },
    {
        "id": 7,
        "img": ASSET_PREFIX + "T202607177441_011_-0eu.avif",
        "caption": "PM inspecting the exhibition gallery of development projects in Chandigarh",
        "date": "17 July 2026",
        "category": "Urban Development"
    },
    {
        "id": 8,
        "img": ASSET_PREFIX + "T202607177440_014_-0eu.avif",
        "caption": "PM interacting with school children onboard India’s first Hydrogen train between Jind and Sonipat at Jind railway station",
        "date": "17 July 2026",
        "category": "Innovation & Railways"
    },
    {
        "id": 9,
        "img": ASSET_PREFIX + "T202607177439_014_-0eu.avif",
        "caption": "PM inspecting the driver cabin of India’s first Hydrogen train at Jind railway station, in Haryana",
        "date": "17 July 2026",
        "category": "Green Transportation"
    },
    {
        "id": 10,
        "img": ASSET_PREFIX + "T202607177438_013_-0eu.avif",
        "caption": "PM flags off India’s first Hydrogen train between Jind and Sonipat at Jind railway station, in Haryana",
        "date": "17 July 2026",
        "category": "Railways & Clean Energy"
    }
]

pm_links = [
    {"title": "PMO Releases", "url": "/del/en/pmo-releases", "desc": "Official press notes from the Prime Minister's Office"},
    {"title": "Speeches", "url": "/del/en/press-releases?ministry=3", "desc": "Keynote addresses and national speeches"},
    {"title": "Photos", "url": "/del/en/galleries?tab=photos", "desc": "High-resolution photo coverage"},
    {"title": "Videos", "url": "/del/en/galleries?tab=videos", "desc": "Live broadcasts and address recordings"},
    {"title": "Visits Abroad", "url": "https://www.pmindia.gov.in/en/pm-visits/", "desc": "Bilateral summits and state visits", "ext": True},
    {"title": "CCEA Decisions", "url": "/del/en/press-releases?ministry=63", "desc": "Cabinet Committee on Economic Affairs"},
    {"title": "Cabinet Decisions", "url": "/del/en/press-releases?ministry=61", "desc": "Union Cabinet policy announcements"},
    {"title": "Connect to PM", "url": "https://www.pmindia.gov.in/", "desc": "Direct citizen interaction via PMINDIA portal", "ext": True}
]

releases_data = [
    {
        "id": "rel-1",
        "title": "National Biodiversity Authority releases Rs. 15.52 crore ABS Proceeds from Mustard Genetic Resources",
        "url": "/del/en/press-releases/national-biodiversity-authority-releases-rs-15-52-crore-abs-proceeds-from-mustar-2298712",
        "ministry": "Ministry of Environment, Forest and Climate Change",
        "date": "13 August 2026",
        "read_time": "9 min read",
        "img": ASSET_PREFIX + "moef_gov_in_-0eu.avif",
        "is_photo": False,
        "bullets": [
            "The National Biodiversity Authority (NBA) has released Rs. 15.52 crore in Access and Benefit Sharing (ABS) proceeds.",
            "Proceeds received from M/s Pioneer Overseas Corporation, which developed ten commercial mustard (Brassica juncea) hybrid varieties using India's biological resources.",
            "Funds allocated to benefit-claimers and Biodiversity Management Committees (BMCs) across relevant state jurisdictions."
        ],
        "top": True,
        "most_read": True
    },
    {
        "id": "rel-2",
        "title": "Prime Minister shares a Sanskrit Subhashitam, highlighting determination, perseverance, and continuous effort in overcoming life's challenges",
        "url": "/del/en/press-releases/prime-minister-shares-a-sanskrit-subhashitam-highlighting-determination-persever-2298710",
        "ministry": "Prime Minister's Office",
        "date": "13 August 2026",
        "read_time": "2 min read",
        "img": ASSET_PREFIX + "wp_3_-0eu.avif",
        "is_photo": False,
        "bullets": [
            "Prime Minister Shri Narendra Modi shared a Sanskrit Subhashitam emphasizing the power of unwavering determination and perseverance.",
            "The PM highlighted: 'A person who possesses determination, perseverance and courage to turn adverse circumstances into favorable ones is never defeated.'",
            "Message calls upon the youth to remain persistent and cultivate inner strength in nation-building."
        ],
        "top": True,
        "most_read": True
    },
    {
        "id": "rel-3",
        "title": "PRESS RELEASE ON 393rd REPORT OF THE DEPARTMENT-RELATED PARLIAMENTARY STANDING COMMITTEE ON TRANSPORT, TOURISM AND CULTURE",
        "url": "/del/en/press-releases/press-release-on-393rd-report-of-the-department-related-parliamentary-standing-c-2298703",
        "ministry": "Parliamentary Standing Committee",
        "date": "12 August 2026",
        "read_time": "8 min read",
        "img": ASSET_PREFIX + "pib-logo_004_-0eu.avif",
        "is_photo": False,
        "bullets": [
            "Report titled 'From Manuscript to Mission: Preserving, Mapping and Sustaining India’s Cultural Heritage in the Age of Artificial Intelligence' presented in Rajya Sabha.",
            "Headed by Shri Sanjay Kumar Jha, M.P., examining AI-driven digitisation of over 45 lakh ancient manuscripts.",
            "Recommends establishment of a National Cultural AI Knowledge Grid and enhanced funding for conservation."
        ],
        "top": True,
        "most_read": False
    },
    {
        "id": "rel-4",
        "title": "India and the Southern African Customs Union (SACU) sign Terms of Reference (ToR) for negotiations towards a Preferential Trade Agreement",
        "url": "/del/en/press-releases/india-and-the-southern-african-customs-union-sacu-sign-terms-of-reference-tor-fo-2298681",
        "ministry": "Ministry of Commerce & Industry",
        "date": "12 August 2026",
        "read_time": "5 min read",
        "img": ASSET_PREFIX + "wp_16_-0eu.avif",
        "is_photo": False,
        "bullets": [
            "Formal Terms of Reference (ToR) signed between India and SACU member states (South Africa, Botswana, Namibia, Lesotho, Eswatini).",
            "Paves path for duty concessions across critical sectors including engineering goods, pharmaceuticals, textiles, and mineral resources.",
            "Bilateral merchandise trade targeted to expand beyond USD 30 billion over the next 5 fiscal years."
        ],
        "top": True,
        "most_read": True
    },
    {
        "id": "rel-5",
        "title": "LOK SABHA SPEAKER HAILS SHRI KOVIND’S STORY AS AN ENDURING SOURCE OF “INSPIRATION FOR GENERATIONS”",
        "url": "/del/en/press-releases/lok-sabha-speaker-hails-shri-kovind-s-story-as-an-enduring-source-of-inspiration-2298663",
        "ministry": "Lok Sabha Secretariat",
        "date": "12 August 2026",
        "read_time": "4 min read",
        "img": ASSET_PREFIX + "wp_2608_003_-0eu.avif",
        "is_photo": False,
        "bullets": [
            "Lok Sabha Speaker Shri Om Birla addresses the gathering at the launch of autobiography of former President Shri Ram Nath Kovind.",
            "Hails the journey from Paraunkh village in Kanpur Dehat to Rashtrapati Bhavan as a testament to the resilience of Indian democracy.",
            "Stresses the importance of institutional integrity and inclusive constitutional values."
        ],
        "top": False,
        "most_read": False
    },
    {
        "id": "rel-6",
        "title": "Digital India BHASHINI Division (DIBD) and NITI Aayog Sign Statement of Intent to Advance Multilingual AI for Inclusive Governance",
        "url": "/del/en/press-releases/digital-india-bhashini-division-dibd-and-niti-aayog-sign-statement-of-intent-to-2298661",
        "ministry": "Ministry of Electronics & IT",
        "date": "12 August 2026",
        "read_time": "6 min read",
        "img": ASSET_PREFIX + "image001Q6QD_002_-0eu.avif",
        "is_photo": True,
        "bullets": [
            "Strategic collaboration to integrate voice-first, vernacular AI translation capabilities across Central and State government citizen services.",
            "Focuses on 22 scheduled Indian languages to bridge the digital literacy divide for rural beneficiaries.",
            "Pilot deployments slated for agriculture advisory, telemedicine support, and social welfare scheme enrolments."
        ],
        "top": True,
        "most_read": True
    },
    {
        "id": "rel-7",
        "title": "Union Home Minister and Minister of Cooperation Shri Amit Shah launches the ‘Gramin Gyan Setu’ app via video conferencing; interconnecting rural libraries",
        "url": "/del/en/press-releases/union-home-minister-and-minister-of-cooperation-shri-amit-shah-launches-the-gram-2298635",
        "ministry": "Ministry of Home Affairs",
        "date": "12 August 2026",
        "read_time": "6 min read",
        "img": ASSET_PREFIX + "wp_5_004_-0eu.avif",
        "is_photo": False,
        "bullets": [
            "Integrates village library networks across Gandhinagar Lok Sabha constituency with over 2.5 lakh e-books and competitive exam resources.",
            "Dedicated on the birth anniversary of Dr. S.R. Ranganathan, father of Indian library science.",
            "Enables smart-device kiosk access in panchayat bhavans with multilingual reading capabilities."
        ],
        "top": True,
        "most_read": False
    },
    {
        "id": "rel-8",
        "title": "National Commission for Scheduled Castes submits Annual Report-2024–25 to Hon’ble President of India, Smt Droupadi Murmu",
        "url": "/del/en/press-releases/national-commission-for-scheduled-castes-submits-annual-report-2024-25-to-hon-bl-2298611",
        "ministry": "Ministry of Social Justice & Empowerment",
        "date": "12 August 2026",
        "read_time": "3 min read",
        "img": ASSET_PREFIX + "image001GTX8_015_-0eu.avif",
        "is_photo": True,
        "bullets": [
            "NCSC delegation led by Chairman presented constitutional compliance review to President Droupadi Murmu at Rashtrapati Bhavan.",
            "Highlights progress in educational scholarship disbursement, entrepreneurship funding under Stand-Up India, and grievance redressal rate.",
            "Recommendations submitted for reinforcing safeguards across unorganized service sectors."
        ],
        "top": False,
        "most_read": False
    },
    {
        "id": "rel-9",
        "title": "Union Health Minister Shri Nadda interacts with MPs from Jharkhand and Odisha to strengthen efforts towards TB Mukt Bharat",
        "url": "/del/en/press-releases/union-health-minister-shri-nadda-interacts-with-mps-from-jharkhand-and-odisha-to-2298602",
        "ministry": "Ministry of Health and Family Welfare",
        "date": "12 August 2026",
        "read_time": "11 min read",
        "img": ASSET_PREFIX + "image0010RSR_014_-0eu.avif",
        "is_photo": True,
        "bullets": [
            "Review of Ni-kshay Mitra nutrition support, molecular diagnostic deployment, and community screening drives.",
            "Special emphasis on tribal belts and industrial mining zones in Jharkhand and Odisha for early case detection.",
            "Expansion of decentralized BPaLM regimen for drug-resistant tuberculosis treatment."
        ],
        "top": False,
        "most_read": True
    },
    {
        "id": "rel-10",
        "title": "Three Sanchar Mitras Selected as ITU Generation Connect Youth Envoys for the period 2026–2030",
        "url": "/del/en/press-releases/three-sanchar-mitras-selected-as-itu-generation-connect-youth-envoys-for-the-per-2298552",
        "ministry": "Ministry of Communications",
        "date": "12 August 2026",
        "read_time": "7 min read",
        "img": ASSET_PREFIX + "wp_24_-0eu.avif",
        "is_photo": False,
        "bullets": [
            "Recognized by the International Telecommunication Union (ITU) for pioneering grassroots digital inclusion initiatives in India.",
            "Envoys will represent India at international summits on telecom standardisation, AI ethics, and broadband access.",
            "Demonstrates youth leadership under DoT’s flagship Sanchar Mitra nationwide campus program."
        ],
        "top": False,
        "most_read": False
    },
    {
        "id": "rel-11",
        "title": "National Company Law Tribunal (NCLT) Launches e-Inspection and e-Certified Copy Services",
        "url": "/del/en/press-releases/national-company-law-tribunal-nclt-launches-e-inspection-and-e-certified-copy-se-2298542",
        "ministry": "Ministry of Corporate Affairs",
        "date": "12 August 2026",
        "read_time": "4 min read",
        "img": ASSET_PREFIX + "_CLP5326_007_-0eu.avif",
        "is_photo": True,
        "bullets": [
            "Hon’ble President NCLT Justice Anupinder Singh Grewal inaugurates end-to-end paperless tribunal services via video conference.",
            "Allows litigants and corporate counsels to inspect records digitally without physical registry visits.",
            "Part of e-Courts 2.0 modernization, slashing certified copy delivery turnaround from 14 days to 24 hours."
        ],
        "top": False,
        "most_read": False
    },
    {
        "id": "rel-12",
        "title": "Smt Archana Varma Takes Charge as Secretary, Department of Water Resources, RD & GR, Ministry of Jal Shakti",
        "url": "/del/en/press-releases/smt-archana-varma-takes-charge-as-secretary-department-of-water-resources-rd-gr-2298538",
        "ministry": "Ministry of Jal Shakti",
        "date": "12 August 2026",
        "read_time": "3 min read",
        "img": ASSET_PREFIX + "image001UVI0_007_-0eu.avif",
        "is_photo": True,
        "bullets": [
            "1995-batch IAS officer of the Assam cadre officially assumes office at Shram Shakti Bhawan, New Delhi.",
            "Prioritizes accelerated completion of inter-linking river projects and groundwater replenishment under Jal Jeevan Mission.",
            "Welcomed by Joint Secretary (Admn.) Shri Karan Singh and senior ministry officials."
        ],
        "top": False,
        "most_read": False
    },
    {
        "id": "rel-13",
        "title": "The Government of India to launch the Central Bank Digital Currency (CBDC)-based Direct Benefit Transfer (DBT) in the Union Territories of Chandigarh and Dadra & Nagar Haveli",
        "url": "/del/en/press-releases/the-government-of-india-to-launch-the-central-bank-digital-currency-cbdc-based-d-2298531",
        "ministry": "Ministry of Finance & Corporate Affairs",
        "date": "12 August 2026",
        "read_time": "4 min read",
        "img": ASSET_PREFIX + "pib-logo_004_-0eu.avif",
        "is_photo": False,
        "bullets": [
            "Programmable digital Rupee (e₹) e-wallets to disburse fertilizer, nutrition, and student scholarship subventions without banking intermediaries.",
            "Enables offline wallet-to-wallet transactions in remote pockets with patchy cellular network coverage.",
            "Guarantees 100% targeted spend fidelity with zero leakage or intermediary deductions."
        ],
        "top": True,
        "most_read": True
    },
    {
        "id": "rel-14",
        "title": "India’s Infrastructure Transformation: From Connectivity to Capacity — A Comprehensive Decade Review",
        "url": "/del/en/press-releases/india-s-infrastructure-transformation-from-connectivity-to-capacity-2298526",
        "ministry": "PIB Headquarters",
        "date": "12 August 2026",
        "read_time": "38 min read",
        "img": ASSET_PREFIX + "image001915I_008_-0eu.avif",
        "is_photo": True,
        "bullets": [
            "Building the Foundation of Growth: In-depth statistical analysis of national highways, dedicated freight corridors, and airport expansions over past 12 years.",
            "Capital expenditure on national infrastructure quadrupled, catalyzing private sector logistics efficiency from 14% to under 9% of GDP.",
            "Detailed chapter breakdowns on PM GatiShakti National Master Plan, BharatNet, and Multi-Modal Logistics Parks."
        ],
        "top": True,
        "most_read": True
    },
    {
        "id": "rel-15",
        "title": "Parliament Question: IGB Meeting Of BRICS Network University",
        "url": "/del/en/press-releases/parliament-question-igb-meeting-of-brics-network-university-2298515",
        "ministry": "Ministry of Education",
        "date": "12 August 2026",
        "read_time": "4 min read",
        "img": ASSET_PREFIX + "wp_8_002_-0eu.avif",
        "is_photo": False,
        "bullets": [
            "During India's BRICS Chairship 2026, Ministry of Education organized the virtual International Governing Board (IGB) session.",
            "Central theme: 'Need and Challenges of Preservation of Traditional and Indigenous Knowledge Systems in the Digital Age'.",
            "Joint academic research protocols, credit transfer pacts, and multilingual translation repositories established across all 10 member states."
        ],
        "top": False,
        "most_read": False
    }
]

explainers_data = [
    {
        "id": "exp-1",
        "title": "India’s Infrastructure Transformation: From Connectivity to Capacity",
        "category": "INFRASTRUCTURE",
        "badge": "Factsheet",
        "date": "12 August 2026",
        "img": ASSET_PREFIX + "image001915I_008_-0eu.avif",
        "is_photo": True,
        "desc": "How integrated multimodal logistics, expressways, and dedicated freight corridors are reshaping India's economic competitiveness.",
        "url": "/del/en/explainers/india-s-infrastructure-transformation-from-connectivity-to-capacity-1000150842"
    },
    {
        "id": "exp-2",
        "title": "Empowering Governance through Digital Infrastructure",
        "category": "TECHNOLOGY",
        "badge": "Factsheet",
        "date": "12 August 2026",
        "img": ASSET_PREFIX + "image001Q6QD_002_-0eu.avif",
        "is_photo": True,
        "desc": "Examining the pillars of India Stack: UPI, DigiLocker, Aadhaar-enabled payments, and the Bhashini multilingual revolution.",
        "url": "/del/en/explainers/empowering-governance-through-digital-infrastructure-1000150840"
    },
    {
        "id": "exp-3",
        "title": "The New Era of Indian Agriculture and Allied Sectors",
        "category": "FARMER'S WELFARE",
        "badge": "Factsheet",
        "date": "12 August 2026",
        "img": ASSET_PREFIX + "moef_gov_in_-0eu.avif",
        "is_photo": False,
        "desc": "Crop diversification, drone technologies, micro-irrigation, and farmer producer organisations (FPOs) driving resilient farm incomes.",
        "url": "/del/en/explainers/the-new-era-of-indian-agriculture-and-allied-sectors-1000150838"
    },
    {
        "id": "exp-4",
        "title": "Affordable and Accessible Healthcare for All",
        "category": "SOCIAL WELFARE",
        "badge": "Factsheet",
        "date": "12 August 2026",
        "img": ASSET_PREFIX + "image0010RSR_014_-0eu.avif",
        "is_photo": True,
        "desc": "Ayushman Bharat PM-JAY coverage expansion, 1.7 lakh Ayushman Arogya Mandirs, and the Pradhan Mantri Bhartiya Janaushadhi Pariyojana.",
        "url": "/del/en/explainers/affordable-and-accessible-healthcare-for-all-1000150834"
    },
    {
        "id": "exp-5",
        "title": "Financial Inclusion in India: Banking Every Citizen, Empowering Every Household",
        "category": "ECONOMY",
        "badge": "Factsheet",
        "date": "12 August 2026",
        "img": ASSET_PREFIX + "wp_16_-0eu.avif",
        "is_photo": False,
        "desc": "A decade of Pradhan Mantri Jan Dhan Yojana (PMJDY), micro-credit under PM SVANidhi, and direct benefit transfer fidelity.",
        "url": "/del/en/explainers/financial-inclusion-in-india-banking-every-citizen-empowering-every-household-1000150832"
    },
    {
        "id": "exp-6",
        "title": "Reforming India’s Tribunal System",
        "category": "SOCIAL WELFARE",
        "badge": "Factsheet",
        "date": "12 August 2026",
        "img": ASSET_PREFIX + "_CLP5326_007_-0eu.avif",
        "is_photo": True,
        "desc": "Modernizing company law, tax, and appellate dispute resolution through unified digital tribunals and e-courts.",
        "url": "/del/en/explainers/reforming-india-s-tribunal-system-1000150828"
    },
    {
        "id": "exp-7",
        "title": "World Elephant Day: Habitat Protection & Human-Elephant Coexistence",
        "category": "ENERGY & ENVIRONMENT",
        "badge": "Backgrounder",
        "date": "12 August 2026",
        "img": ASSET_PREFIX + "image0040M0Q_002_-0eu.avif",
        "is_photo": True,
        "desc": "Project Elephant conservation corridors, satellite radio-collaring, and community early-warning sensors across sanctuary buffers.",
        "url": "/del/en/explainers/world-elephant-day-159528"
    },
    {
        "id": "exp-8",
        "title": "The Micro, Small and Medium Enterprises Development (Amendment) Bill, 2026",
        "category": "ECONOMY",
        "badge": "Factsheet",
        "date": "11 August 2026",
        "img": ASSET_PREFIX + "wp_2608_003_-0eu.avif",
        "is_photo": False,
        "desc": "Key provisions, revised composite investment thresholds, prompt payment safeguards, and credit guarantee enhancements for MSMEs.",
        "url": "/del/en/explainers/the-micro-small-and-medium-enterprises-development-amendment-bill-2026-1000150826"
    }
]

advisories_data = [
    {
        "id": "adv-1",
        "title": "Press Conference on Cabinet decisions at 04:00 PM today i.e. 06.08.2026 at National Media Centre New Delhi. Entry strictly on the basis of PIB Card.",
        "url": "/del/en/media-announcements/press-conference-on-cabinet-decisions-at-04-00-pm-today-i-e-06-08-2026-at-nation-618",
        "date": "06 August 2026",
        "time": "04:00 PM IST",
        "venue": "National Media Centre, Raisina Road, New Delhi",
        "req": "Entry strictly on the basis of valid PIB Accreditation Card"
    },
    {
        "id": "adv-2",
        "title": "Press Conference on Cabinet decisions at 04:00 PM today i.e. 31.07.2026 at National Media Centre New Delhi. Entry strictly on the basis of PIB Card.",
        "url": "/del/en/media-announcements/press-conference-on-cabinet-decisions-at-04-00-pm-today-i-e-31-07-2026-at-nation-617",
        "date": "31 July 2026",
        "time": "04:00 PM IST",
        "venue": "National Media Centre, Raisina Road, New Delhi",
        "req": "Entry strictly on the basis of valid PIB Accreditation Card"
    },
    {
        "id": "adv-3",
        "title": "Media Alert: Press Conference on Cabinet decisions at 04:00 PM today i.e. 24.07.2026 at National Media Centre New Delhi. Entry strictly on the basis of PIB Card",
        "url": "/del/en/media-announcements/media-alert-press-conference-on-cabinet-decisions-at-04-00-pm-today-i-e-24-07-20-616",
        "date": "24 July 2026",
        "time": "04:00 PM IST",
        "venue": "National Media Centre, Raisina Road, New Delhi",
        "req": "Entry strictly on the basis of valid PIB Accreditation Card"
    }
]

videos_data = [
    {
        "id": 1,
        "title": "Cabinet Briefing by Union Minister Ashwini Vaishnaw",
        "date": "06 August 2026",
        "img": ASSET_PREFIX + "hqdefault_102_-0eu.avif",
        "tag": "Union Cabinet Briefing",
        "duration": "48:15"
    },
    {
        "id": 2,
        "title": "PIB Special Briefing: Key Governance Reforms",
        "date": "22 July 2026",
        "img": ASSET_PREFIX + "hqdefault_099_-0eu.avif",
        "tag": "Media Briefing",
        "duration": "32:40"
    },
    {
        "id": 3,
        "title": "PM Modi participates in a community event in Auckland, New Zealand",
        "date": "11 July 2026",
        "img": ASSET_PREFIX + "hqdefault_086_-0eu.avif",
        "tag": "Diaspora Address",
        "duration": "1:15:20"
    },
    {
        "id": 4,
        "title": "PM Modi participates in a community event in Melbourne, Australia",
        "date": "09 July 2026",
        "img": ASSET_PREFIX + "hqdefault_135_-0eu.avif",
        "tag": "Diaspora Address",
        "duration": "58:45"
    },
    {
        "id": 5,
        "title": "Cabinet Briefing by Union Minister Ashwini Vaishnaw",
        "date": "01 July 2026",
        "img": ASSET_PREFIX + "hqdefault_042_-0eu.avif",
        "tag": "Union Cabinet Briefing",
        "duration": "42:10"
    },
    {
        "id": 6,
        "title": "Inter-Ministerial Briefing on Recent Developments in West Asia",
        "date": "18 June 2026",
        "img": ASSET_PREFIX + "hqdefault_021_-0eu.avif",
        "tag": "External Affairs",
        "duration": "28:35"
    },
    {
        "id": 7,
        "title": "Inter-Ministerial Briefing on Recent Developments in West Asia",
        "date": "15 June 2026",
        "img": ASSET_PREFIX + "hqdefault_129_-0eu.avif",
        "tag": "External Affairs",
        "duration": "25:50"
    },
    {
        "id": 8,
        "title": "PM Modi attends the NITI Aayog Governing Council Meeting",
        "date": "11 June 2026",
        "img": ASSET_PREFIX + "hqdefault_125_-0eu.avif",
        "tag": "NITI Aayog",
        "duration": "51:00"
    },
    {
        "id": 9,
        "title": "Cabinet Briefing by Union Minister Ashwini Vaishnaw",
        "date": "10 June 2026",
        "img": ASSET_PREFIX + "hqdefault_038_-0eu.avif",
        "tag": "Union Cabinet Briefing",
        "duration": "39:18"
    },
    {
        "id": 10,
        "title": "PM Modi lays foundation stone, inaugurates various development works in Daman",
        "date": "05 June 2026",
        "img": ASSET_PREFIX + "hqdefault_016_-0eu.avif",
        "tag": "Development Works",
        "duration": "1:04:12"
    }
]

photos_data = [
    {
        "id": 1,
        "img": ASSET_PREFIX + "T20260812214418_-0eu.JPG",
        "caption": "Gathering at the event of Release of Autobiography of former President of India, Shri Ram Nath Kovind, titled 'Triumph of the Indian Republic: My Life, My Struggles' at Vigyan Bhavan, New Delhi. PM addressing on the occasion.",
        "date": "12 August 2026",
        "location": "Vigyan Bhawan, New Delhi"
    },
    {
        "id": 2,
        "img": ASSET_PREFIX + "T20260812214416_005_-0eu.avif",
        "caption": "PM addressing the gathering on the occasion of Release of Autobiography of former President Shri Ram Nath Kovind at Vigyan Bhavan, New Delhi.",
        "date": "12 August 2026",
        "location": "Vigyan Bhawan, New Delhi"
    },
    {
        "id": 3,
        "img": ASSET_PREFIX + "T20260812214413_013_-0eu.avif",
        "caption": "PM graced the occasion of Release of Autobiography of former President Shri Ram Nath Kovind with distinguished dignitaries.",
        "date": "12 August 2026",
        "location": "Vigyan Bhawan, New Delhi"
    },
    {
        "id": 4,
        "img": ASSET_PREFIX + "T20260812214409_004_-0eu.avif",
        "caption": "PM releases the autobiography of former President Shri Ram Nath Kovind, titled 'Triumph of the Indian Republic: My Life, My Struggles'.",
        "date": "12 August 2026",
        "location": "Vigyan Bhawan, New Delhi"
    },
    {
        "id": 5,
        "img": ASSET_PREFIX + "T20260812214444_014_-0eu.avif",
        "caption": "Union Minister for Agriculture & Farmers Welfare and Rural Development, Shri Shivraj Singh addressing the gathering at national farm summit.",
        "date": "12 August 2026",
        "location": "New Delhi"
    },
    {
        "id": 6,
        "img": ASSET_PREFIX + "T20260812214439_011_-0eu.avif",
        "caption": "Union Minister for Agriculture & Farmers Welfare Shri Shivraj Singh participating in the national agriculture mission session.",
        "date": "12 August 2026",
        "location": "New Delhi"
    },
    {
        "id": 7,
        "img": ASSET_PREFIX + "T20260812214426_013_-0eu.avif",
        "caption": "Union Minister of Culture and Tourism Shri Gajendra Singh Shekhawat and Union Minister of Coal and Mines Shri G. Kishan Reddy at cultural preservation conclave.",
        "date": "12 August 2026",
        "location": "New Delhi"
    },
    {
        "id": 8,
        "img": ASSET_PREFIX + "T20260812214434_002_-0eu.avif",
        "caption": "Union Minister of Textiles Shri Giriraj Singh addressing at the inauguration of the first Annual Conclave of the Indian Institute of Handloom Technology.",
        "date": "12 August 2026",
        "location": "New Delhi"
    },
    {
        "id": 9,
        "img": ASSET_PREFIX + "T20260812214428_012_-0eu.avif",
        "caption": "Union Minister of Textiles Shri Giriraj Singh inspecting handloom innovations at the inauguration of IIHT Annual Conclave.",
        "date": "12 August 2026",
        "location": "New Delhi"
    },
    {
        "id": 10,
        "img": ASSET_PREFIX + "T20260812214427_013_-0eu.avif",
        "caption": "Union Minister of Textiles Shri Giriraj Singh lighting the traditional ceremonial lamp at the inauguration of the first Annual Conclave of IIHT.",
        "date": "12 August 2026",
        "location": "New Delhi"
    }
]

blogs_data = [
    {
        "id": 1,
        "title": "11 Years of Modi: Fuelled by Vision, Powered by Energy",
        "url": "/del/en/blogs/11-years-of-modi-fuelled-by-vision-powered-by-energy-169",
        "img": ASSET_PREFIX + "I20250604309_005_-0eu.avif",
        "date": "04 June 2025",
        "tag": "Governance & Vision",
        "desc": "How clear policy direction and sustained reforms have transformed India's domestic energy security, infrastructure, and international standing."
    },
    {
        "id": 2,
        "title": "Viksit Krishi Sankalp Abhiyan will achieve the mantra of ‘Lab-to-Land’",
        "url": "/del/en/blogs/viksit-krishi-sankalp-abhiyan-will-achieve-the-mantra-of-lab-to-land-166",
        "img": ASSET_PREFIX + "I20250604306_014_-0eu.avif",
        "date": "04 June 2025",
        "tag": "Agriculture",
        "desc": "Bridging agronomy research laboratories with farm cultivators to maximize per-hectare yield and climate-resilient organic agriculture."
    },
    {
        "id": 3,
        "title": "Powering a Green Future: How 11 Years of Modi Government Changed India’s Renewable Energy Sector",
        "url": "/del/en/blogs/powering-a-green-future-how-11-years-of-modi-government-changed-india-s-renewabl-164",
        "img": ASSET_PREFIX + "I20250604303_012_-0eu.avif",
        "date": "04 June 2025",
        "tag": "Clean Energy",
        "desc": "Scaling solar, wind, and green hydrogen capacity from 35 GW in 2014 to over 190 GW today, placing India 4th globally."
    },
    {
        "id": 4,
        "title": "Treating TB beyond medicine",
        "url": "/del/en/blogs/treating-tb-beyond-medicine-162",
        "img": ASSET_PREFIX + "I20250530302_013_-0eu.avif",
        "date": "30 May 2025",
        "tag": "Public Health",
        "desc": "Why community nutritional support, social stigma eradication, and Ni-kshay Mitra networks are decisive in eliminating tuberculosis."
    },
    {
        "id": 5,
        "title": "Operation Sindoor: Where National Security meets National Honour",
        "url": "/del/en/blogs/operation-sindoor-where-national-security-meets-national-honour-158",
        "img": ASSET_PREFIX + "I20250521298_006_-0eu.avif",
        "date": "21 May 2025",
        "tag": "National Defence",
        "desc": "A tribute to the synchronized valour and indigenous technological superiority of the Armed Forces in safeguarding territorial sovereignty."
    },
    {
        "id": 6,
        "title": "GeM – Making Public Procurement sparkle",
        "url": "/del/en/blogs/gem-making-public-procurement-sparkle-156",
        "img": ASSET_PREFIX + "I20250521296_008_-0eu.avif",
        "date": "21 May 2025",
        "tag": "Digital Governance",
        "desc": "How the Government e-Marketplace democratized state procurement, allowing small rural artisans and women entrepreneurs to sell to the state."
    },
    {
        "id": 7,
        "title": "Operation Sindoor: A Decisive Victory in Modern Warfare",
        "url": "/del/en/blogs/operation-sindoor-a-decisive-victory-in-modern-warfare-153",
        "img": ASSET_PREFIX + "I20250516293_011_-0eu.avif",
        "date": "16 May 2025",
        "tag": "Strategic Studies",
        "desc": "Analysis of multi-domain integration, satellite-guided precision strikes, and counter-terror tactical operations."
    },
    {
        "id": 8,
        "title": "Modi doctrine on dealing with terror: Operation Sindoor",
        "url": "/del/en/blogs/modi-doctrine-on-dealing-with-terror-operation-sindoor-151",
        "img": ASSET_PREFIX + "I20250514291_008_-0eu.avif",
        "date": "14 May 2025",
        "tag": "Strategic Policy",
        "desc": "Zero tolerance, pre-emptive response, and international diplomatic isolation: the defining tenets of India's robust counter-terror doctrine."
    },
    {
        "id": 9,
        "title": "WAVES: Nurturing Young Creators & Accelerating India's M&E Startups for Global Impact",
        "url": "/del/en/blogs/waves-nurturing-young-creators-accelerating-india-s-m-e-startups-for-global-impa-149",
        "img": ASSET_PREFIX + "I20250430289_007_-0eu.avif",
        "date": "30 April 2025",
        "tag": "Creative Economy",
        "desc": "Empowering content creators, animation artists, VFX studios, and gaming entrepreneurs through the World Audio Visual & Entertainment Summit."
    },
    {
        "id": 10,
        "title": "Tech Versus Tradition: Immersive Revolution in Indian Cinema",
        "url": "/del/en/blogs/tech-versus-tradition-immersive-revolution-in-indian-cinema-147",
        "img": ASSET_PREFIX + "I20250430287_003_-0eu.avif",
        "date": "30 April 2025",
        "tag": "Cinema & Culture",
        "desc": "How virtual production, AI soundscapes, and digital restoration are elevating classic Indian storytelling for 21st-century global cinephiles."
    },
    {
        "id": 11,
        "title": "WAVES 2025: India’s Leap Towards Global Creative Leadership",
        "url": "/del/en/blogs/waves-2025-india-s-leap-towards-global-creative-leadership-145",
        "img": ASSET_PREFIX + "I20250429285_009_-0eu.avif",
        "date": "29 April 2025",
        "tag": "Global Summit",
        "desc": "Establishing India as the world's premier destination for audiovisual co-productions, intellectual property incubation, and creative talent."
    },
    {
        "id": 12,
        "title": "The Future of Indian Entertainment: From Jugaad (quickfixes) to Global Greatness",
        "url": "/del/en/blogs/the-future-of-indian-entertainment-from-jugaad-quickfixes-to-global-greatness-139",
        "img": ASSET_PREFIX + "pib-logo_006_-0eu.avif",
        "date": "21 April 2025",
        "tag": "Industry Analysis",
        "desc": "Transitioning from ad-hoc production compromises to world-class studio pipelines, IP ownership, and international distribution dominance."
    }
]

print("Datasets loaded. Now constructing full HTML template...")
