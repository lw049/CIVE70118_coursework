# Application of discrete choice models in policy impact analysis

**Coursework**  
**CIVE70016:** Transport Demand and Economics  
**CIVE70118:** Transport Economics and Demand  

* **Handed out:** 4 November 2026
* **Submission due:** 11 December 2026 05:00 PM via Canvas

Only one submission per group is needed. Submission must include:
1. **Group coursework report** (no min length; length not to exceed 25 pages including tables and figures; appendices may be included as evidence but scoring will be based only on the main body of the report)
2. **Recorded group presentation** (max 15 minutes, any video format that can be viewed by non-proprietary software, preferably mp4 or avi)
3. **Statement of individual contribution** signed by all members of the group

**Prof Aruna Sivakumar**  
Centre for Transport Engineering and Modelling  
Department of Civil and Environmental Engineering  
Imperial College London  
London SW7 2AZ  
November 2026

---

## Scope

Working as a group (see Group Allocations at the end of this document), your task is to consider the transport planning topic assigned to you (Topic Details available further below) and assess the impacts of the policy interventions suggested.

You are provided with a travel survey dataset as indicated by the dataset number next to your topic; an accompanying data dictionary is also provided. If you have columns with missing values you need to decide how best to deal with it. Your task as a group is to estimate an appropriate travel demand model with your dataset using discrete choice modelling (DCM) methodology, and to apply the model to test the suggested interventions and therefore identify the preferred intervention. Ensure any assumptions made are clearly documented.

Here are some recommended sections and questions that will help you structure and present your analysis. The presentations and reports should cover all these areas.

1. **Define the challenge**
   * a. What is the objective of the policy?
   * b. What could be the motivations underlying these objectives i.e. overall goal?
   * c. Who are the potential stakeholders?
2. **Develop the conceptual approach**
   * a. What are your proposed interventions to be tested?
   * b. Are they realistic and feasible?
   * c. Have you selected interventions that can be modelled using the data provided?
3. **Design an appropriate DCM model using the data provided**
   * a. How to model your interventions using a DCM?
   * b. Which alternatives do you need to consider?
   * c. Which variables from your dataset need to enter your model specification?
4. **Estimate DCM specifications using the dataset provided**
   * a. Which specification is optimal? Is nesting required?
   * b. Does your specification allow you to model the impact of the interventions?
5. **Apply the estimated DCM to assess the impact of the proposed intervention(s)**
   * a. How do probabilities and market shares change under the different interventions?
   * b. Which intervention is more effective at achieving the intended objectives?
6. **What are your recommendations:**
   * a. Are the proposed interventions likely to be effective, in light of your results? Why?
   * b. What are the limitations of your analysis? How can it be practically improved?

---

## Outputs and Assessment

As the outputs of your analysis, you are required to prepare the following. One copy of these deliverables to be submitted per group, via Canvas, by the deadline:

1. **A recorded group presentation**, of maximum length 15 minutes, outlining your overall approach, modelling results and policy recommendations. This will be evaluated by a panel of industry stakeholders and comprises **30%** of your overall coursework mark.
2. **A group coursework report** (no minimum length, maximum length not to exceed 25 pages including figures and tables), summarising your work. The coursework report will constitute **70%** of your overall coursework mark.
3. **A statement of individual contribution**, specifying the contribution from each group member and signed by all group members.

Answers should be typewritten; handwritten submissions will not be accepted. Report all your numerical answers to 3 or 4 decimal places, and be consistent. All notation and variable names should be clearly introduced.

---

## Topic Details

Below is the list of topics to investigate. Each topic outlines the high-level challenge, nature of the interventions to investigate, dataset to use, as well as an additional impact perspective to investigate in your analysis.

### MSc Topics

#### Topic 1: Improvement of walkability in an area by either reducing travel time or improving walking environment
* **Objective:** To increase share of walking trips at the expense of car trips
* **Intervention 1:** Pedestrianise several routes in the area, i.e. reduce walk travel times and increase travel times for car
* **Intervention 2:** Improve public space for walking, i.e. increase walkability index
* **Dataset:** Dataset 1
* **Investigate:** Impacts across age and income groups

#### Topic 2: Improvement in public transport by considering increased frequency of service or reducing ticket price via subsidies
* **Objective:** To shift car-based travelers towards using public transport
* **Intervention 1:** Increase frequency of public transport services, i.e. reduced waiting time for public transport
* **Intervention 2:** Subsidise public transport tickets, i.e. reduce public transport fare
* **Dataset:** Dataset 1
* **Investigate:** Impacts across age and income groups

#### Topic 3: Promote uptake of cycling by considering shortening cycling routes or improvement in the bikeability of the area
* **Objective:** To increase the uptake of cycling
* **Intervention 1:** Expand the cycling network to provide shorter cycling routes, i.e. reduce cycling travel time
* **Intervention 2:** Improve existing cycling infrastructure, i.e. increase bikeability index
* **Dataset:** Dataset 1
* **Investigate:** Impacts across car ownership and age groups

#### Topic 4: Micromobility-based access to public transport
* **Objective:** To improve access to public transport by introducing micromobility service that shortens access time
* **Intervention 1:** Slower but free micromobility for public transport users, i.e. maintain access time but reduce access cost
* **Intervention 2:** More expensive but faster micromobility for public transport users, i.e. maintain access cost but reduce access time
* **Dataset:** Dataset 1
* **Investigate:** Impacts across gender and age groups

#### Topic 5: Introduction of road user charges for cars
* **Objective:** To reduce general use of cars and promote use of other modes of transport
* **Intervention 1:** Introduce flat per trip road user charge that uniformly increases the congestion charge
* **Intervention 2:** Introduce per-mile user charge (assume the speed of 20 mph) that increases the congestion charge in proportion to the distance
* **Dataset:** Dataset 1
* **Investigate:** Impacts across car ownership and income groups

#### Topic 6: Modernising rail to become high-speed
* **Objective:** To increase share of rail trips and reduce car trips
* **Intervention 1:** Improved rolling stock that reduces rail travel time but increases travel costs
* **Intervention 2:** Increase frequency of the current rail service that reduces the waiting time but with no change to travel time or cost
* **Dataset:** Dataset 2
* **Investigate:** Impact across income and gender groups

#### Topic 7: Airport modernisation
* **Objective:** Revitalise the local airport to attract more passengers
* **Intervention 1:** Improving airport capacity leading to a reduction in waiting time
* **Intervention 2:** Improving access to the airport, reducing access time
* **Dataset:** Dataset 2
* **Investigate:** Impact across income, age and gender groups

#### Topic 8: Reduction in train services
* **Objective:** To reduce, due to budget constraints, train services whilst minimising the negative impact on rail's market share
* **Intervention 1:** Removal of night-time services, removing availability of night-time services
* **Intervention 2:** Reducing frequency of services across the entire day, increasing the waiting time
* **Dataset:** Dataset 2
* **Investigate:** Impact across age and income groups

#### Topic 9: Modernisation of night-time coach services
* **Objective:** Increase the market share of coach
* **Intervention 1:** Introduction of reduced-price fares on coach services where an overnight service exists
* **Intervention 2:** Reduce wait time on coach services where an overnight service exists
* **Dataset:** Dataset 2
* **Investigate:** Impact across gender and age groups

#### Topic 10: Promote electric vehicle (EV) uptake through the introduction of EV subsidies and/or taxes on internal combustion engine (ICE) vehicles
* **Objective:** Reduce pollution in cities by encouraging EV adoption, helping to achieve net zero targets
* **Intervention 1:** Subsidise the purchase prices of EVs
* **Intervention 2:** Introduce a tax on the purchase prices of ICE vehicles
* **Dataset:** Dataset 4
* **Investigate:** Impact across education level and age groups

#### Topic 11: Promote the adoption of electric vehicles (EVs), by incentivising EV technology research and development
* **Objective:** Reduce pollution in cities by encouraging EV adoption, helping to achieve net zero targets
* **Intervention 1:** Provide enhanced green technology R&D tax credits, including for battery technologies, aimed at improving EV range
* **Intervention 2:** Provide charging technology R&D grants, aimed at reducing EV charge times
* **Dataset:** Dataset 4
* **Investigate:** Impact across age and income groups

#### Topic 12: Improvement in public transport by considering increased frequency of service or reducing ticket price via subsidies
* **Objective:** To shift car-based travellers towards using public transport
* **Intervention 1:** Increase frequency of public transport services, i.e. reduced waiting time for public transport
* **Intervention 2:** Subsidise public transport tickets, i.e. reduce public transport fare
* **Dataset:** Dataset 1
* **Investigate:** Impacts across age and income groups

---

### MEng Topics

#### Topic A: Promote uptake of cycling by considering shortening cycling routes or improvement in the bikeability of the area
* **Objective:** To increase the uptake of cycling
* **Intervention 1:** Expand the cycling network to provide shorter cycling routes, i.e. reduce cycling travel time
* **Intervention 2:** Improve existing cycling infrastructure, i.e. increase bikeability index
* **Dataset:** Dataset 1
* **Investigate:** Impacts across car ownership and age groups

#### Topic B: Promote electric vehicle (EV) uptake through the introduction of EV subsidies and/or taxes on internal combustion engine (ICE) vehicles
* **Objective:** Reduce pollution in cities by encouraging EV adoption, helping to achieve net zero targets
* **Intervention 1:** Subsidise the purchase prices of EVs
* **Intervention 2:** Introduce a tax on the purchase prices of ICE vehicles
* **Dataset:** Dataset 4
* **Investigate:** Impact across education level and age groups

#### Topic C: Micromobility-based access to public transport
* **Objective:** To improve access to public transport by introducing micromobility service that shortens access time
* **Intervention 1:** Slower but free micromobility for public transport users, i.e. maintain access time but reduce access cost
* **Intervention 2:** More expensive but faster micromobility for public transport users, i.e. maintain access cost but reduce access time
* **Dataset:** Dataset 1
* **Investigate:** Impacts across gender and age groups

#### Topic D: Introduction of road user charges for cars
* **Objective:** To reduce general use of cars and promote use of other modes of transport
* **Intervention 1:** Introduce flat per trip road user charge that uniformly increases the congestion charge
* **Intervention 2:** Introduce per-mile user charge (assume the speed of 20 mph) that increases the congestion charge in proportion to the distance
* **Dataset:** Dataset 1
* **Investigate:** Impacts across car ownership and income groups

#### Topic E: Modernising rail to become high-speed
* **Objective:** To increase share of rail trips and reduce car trips
* **Intervention 1:** Improved rolling stock that reduces travel time but increases travel costs
* **Intervention 2:** Increase frequency of the current rail service that reduces the waiting time but with no change to travel time or cost
* **Dataset:** Dataset 2
* **Investigate:** Impact across income and gender groups

#### Topic F: Airport modernisation
* **Objective:** Revitalise the local airport to attract more passengers
* **Intervention 1:** Improving airport capacity leading to a reduction in waiting time
* **Intervention 2:** Improving access to the airport, reducing access time
* **Dataset:** Dataset 2
* **Investigate:** Impact across income, age and gender groups

#### Topic G: Promote the adoption of electric vehicle (EV) technologies by funding charging and vehicle-to-grid (V2G) infrastructure
* **Objective:** Reduce pollution in cities by encouraging EV adoption, helping to achieve net zero targets
* **Intervention 1:** Fund EV charging and servicing infrastructure development, increasing infrastructure accessibility and reducing maintenance costs
* **Intervention 2:** Fund V2G roll out, reducing net charging costs as EV users can profit from discharging energy back to the electricity grid
* **Dataset:** Dataset 4
* **Investigate:** Impact across gender and household size groups

---

## Group Allocations

### MSc Groups

| Topic - MSc Group | Group members |
| :--- | :--- |
| **Topic 1 - Group MSc1** | Nicolas Barrin<br>Siyao Cai<br>Chhetri Ren<br>Ellis Down<br>Jinmian Ji<br>Ziyue Gao |
| **Topic 2 - Group MSc2** | Kunyu Duan<br>Alexander Grob<br>Emir Hut<br>Chuxin Chen<br>Jaden Feng<br>Stanislas Harland |
| **Topic 3 - Group MSc3** | Arzu Guliyeva<br>ZIJING Lyu<br>Hongyan Xiao<br>Yanrui Zhu<br>Meng Zhao<br>David Tong |
| **Topic 4 - Group MSc4** | Jieying Chen<br>Thibault Lapierre<br>Pathitta Parichartpreecha<br>Ye Tang<br>Qiqian Zeng<br>Haoyang Wang |
| **Topic 5 - Group MSc5** | Elman Aghayev<br>Muze Li<br>Jiani Wei<br>Paweeta Wintachai<br>Ziyu Zhang<br>Tianlun Wang |
| **Topic 6 - Group MSc6** | Guo CHENG<br>Letao Yang<br>Kelvin Oluku<br>MINZHEN Lai<br>Xuan Rong<br>Mahammadali Alizada |
| **Topic 7 - Group MSc7** | Juan Camilo Castrillon Rojas<br>KEMING Huang<br>Xiyue Xing<br>Wenyue Zhou<br>Yelei Zhu |
| **Topic 8 - Group MSc8** | Feier Han<br>Amy Liu<br>Mahendra Nugrohoputra<br>Rory Summerton<br>Cong Wang<br>Xinyi Cao |
| **Topic 9 - Group MSc9** | Jingyao Chen<br>Rahmat Hidayat<br>Jinzhu Ju<br>Yixue Li<br>Daniel Lu<br>Yuxuan Liu |
| **Topic 10 - Group MSc10** | Yunqiu Li<br>Taimin Ning<br>John THU<br>Jingran Zhang<br>Zhicheng Gu<br>Ziyu Wang |
| **Topic 11 - Group MSc11** | Jingyi Chen<br>Crispin Leung<br>Meiqi Niu<br>Zexuan Zhang<br>Jingyi Zhao<br>Allen Yao |
| **Topic 12 - Group MSc12** | Dimitri Bassil<br>JINJING Mao<br>Mengzhu Yuan<br>Raphaelle Benoist<br>Yuelin Qian<br>Lucas Wolman |

### MEng Groups

| Topic - MEng Group | Group members |
| :--- | :--- |
| **Topic A - Group MEng1** | Tom Perry<br>Jack Kwok<br>Cadey Lange<br>Vraj Patel<br>Steve Zheng<br>Jason Young Kim Fat |
| **Topic B - Group MEng2** | Kyle Lee (dropped out)<br>Yibin Zhang (added)<br>Melitini Makridi<br>Hongxiang Simon Ye<br>Bowen Shi<br>Ka Daryn Liu<br>Minsung Kim |
| **Topic C - Group MEng3** | Jinhong Zhu<br>Xintong Chloe Liu<br>Tsz Nelson Chan<br>Hoi Eddie Wong<br>Yeuk Tiffany Leung |
| **Topic D - Group MEng4** | Hamza Hamed<br>Jihua Ye<br>Yirui Xu<br>Miguel Perez Tena<br>Xiaoyu Christina Chen |
| **Topic E - Group MEng5** | Zixin Cindy Wu<br>Kamilla Tleuova<br>Jofre Faraudo Domínguez<br>Lily Payne<br>Rassim Lagha<br>Amy Folgheraiter |
| **Topic F - Group MEng6** | Zhong Lyu<br>Zhuo Chai<br>Yujin Choi<br>David Joshua Catapang<br>Wing Hin Lau |
| **Topic G - Group MEng7** | Nicholas Eastwood<br>Christian Tan<br>Miguel Perez-Pla (dropped out)<br>Yichuan Wang<br>Roya Bernard<br>Job Groot (added) |