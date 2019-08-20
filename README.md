# News-Suggestions-Using-ML
An implementation of LDA in Python to extract lists of topics relevant to article text input by a user. API calls utilizing extracted topics populate news suggestions.

Here, the algorithm identifies ten topic categories related to a gun violence article and suggests ten additional articles from the NYTimes through an API call related to each topic category.

Sample article used from NYTimes: https://www.nytimes.com/2019/08/19/us/politics/trump-gun-laws.html

### Topics generated:

Topic 1: ['trump', 'mass', 'legislation', 'aggressive', 'house', 'response', 'week', 'white', 'shootings', 'back'] 

Topic 2: ['gun', 'trump', 'advocates', 'washington', 'shootings', 'rights', 'checks', 'mass', 'background', 'new']

Topic 3: ['background', 'support', 'trump', 'checks', 'gun', 'shooting', 'bill', 'universal', 'young', 'guns'] 

Topic 4: ['schumer', 'said', 'universal', 'pelosi', 'background', 'trump', 'ms', 'aides', 'check', 'comments'] 

Topic 5: ['said', 'trump', 'people', 'mental', 'health', 'problem', 'forget', 'politics', 'want', 'reshaping'] 

Topic 6: ['president', 'checks', 'something', 'republicans', 'bipartisan', 'democratic', 'hill', 'capitol', 'hard', 'pressure'] 

Topic 7: ['officials', 'trump', 'organization', 'president', 'gun', 'rights', 'statement', 'group', 'muscle', 'internal'] 

Topic 8: ['trump', 'senator', 'republicans', 'laws', 'democrat', 'legislative', 'many', 'house', 'president', 'lawmakers'] 

Topic 9: ['gun', 'safety', 'noted', 'country', 'many', 'feinblatt', 'looking', 'group', 'back', 'white'] 

Topic 10: ['trump', 'gun', 'shooting', 'bedminster', 'pushing', 'senator', 'advocates', 'republican', 'laws', 'tougher'] 


### News Suggestions generated:

**trump mass legislation aggressive house response week white shootings back**
1. After President Trump attacked four congresswomen of color on Twitter, suggesting they "go back" to the places they came from, readers shared experiences of being told the same thing.  https://www.nytimes.com/2019/07/19/reader-center/trump-go-back-stories.html 
2. A cluster of recent mass shootings that killed 36 people in California, Texas and Ohio has sparked renewed calls for the U.S. Congress to pass legislation to prevent gun violence. https://www.nytimes.com/reuters/2019/08/08/us/politics/08reuters-usa-shooting-legislation-factbox.html 
3. A cluster of recent mass shootings that killed 36 people in California, Texas and Ohio has sparked renewed calls for the U.S. Congress to pass legislation to prevent gun violence. https://www.nytimes.com/reuters/2019/08/07/us/07reuters-usa-shooting-legislation-factbox.html 
4. Democrats pressed Senate Majority Leader Mitch McConnell on Tuesday to approve House-passed legislation expanding background checks and to take other steps curbing guns, in an offensive fueled by public outrage over this month's mass killings in T... https://www.nytimes.com/aponline/2019/08/13/us/politics/ap-us-mass-shootings-democrats.html 
5. Democratic presidential candidates have demanded action on proposals to curtail gun violence in the aftermath of two mass shootings that killed 31 people in Texas and Ohio over the weekend. https://www.nytimes.com/reuters/2019/08/07/us/politics/06reuters-usa-election-guns-factbox.html 
6. A cluster of recent mass shootings that killed 36 people in California, Texas and Ohio has sparked renewed calls for the U.S. Congress to pass legislation to prevent gun violence. https://www.nytimes.com/reuters/2019/08/06/us/06reuters-usa-shooting-legislation-factbox.html 
7. Senate Majority Leader Mitch McConnell is resisting pressure to bring senators back from recess to address gun violence, despite wrenching calls to "do something" in the aftermath of back-to-back mass shootings. https://www.nytimes.com/aponline/2019/08/07/us/politics/ap-us-mass-shootings-republicans.html 
8. Some criticism of the president’s stance on gun control and his relationship to the rise of white nationalism came from conservative outlets. https://www.nytimes.com/2019/08/05/business/media/trump-shooting-media-coverage.html 
9. House Speaker Nancy Pelosi said Friday that the country's elected officials have a responsibility to "ensure domestic tranquility" and called on the Senate to return to work to vote on the House's bill bolstering background checks for gun purchase... https://www.nytimes.com/aponline/2019/08/16/us/politics/ap-us-congress-guns.html 
10. Whether the president’s support is real or another momentary reversal will determine if Congress passes the first new federal gun control measures in years. https://www.nytimes.com/2019/08/09/us/politics/gun-background-checks.html 

**gun trump advocates washington shootings rights checks mass background new**
1. In the aftermath of the back-to-back shooting massacres in Texas and Ohio , the debate over gun control has returned to the National Rifle Association and its immense power to stymie any significant legislation on the issue. https://www.nytimes.com/aponline/2019/08/09/us/ap-us-nra-wayne-lapierre-abridged.html 
2. In the aftermath of the back-to-back shooting massacres in Texas and Ohio, the debate over gun control has returned to the National Rifle Association and its immense power to stymie any significant legislation on the issue. https://www.nytimes.com/aponline/2019/08/08/us/ap-us-nra-wayne-lapierre.html 
3. The F.B.I. also said it had opened a domestic terrorism investigation into the shooting at a Gilroy, Calif., garlic festival. https://www.nytimes.com/2019/08/06/us/mass-shootings.html 
4. His presidency hasn’t been the boon for gun-rights supporters that they might have hoped. https://www.nytimes.com/2019/02/11/opinion/trump-nra-parkland.html 
5. “Our officers need help, they need help with gun control,” Philadelphia’s mayor said after six police officers were wounded by gunfire. But in most states, the issue is not up to urban leaders. https://www.nytimes.com/2019/08/15/us/philadelphia-shooting-gun-control.html 
6. If the president did not originally inspire the gunman, he has brought into the mainstream polarizing ideas and people once consigned to the fringes of American society. https://www.nytimes.com/2019/08/04/us/politics/trump-mass-shootings.html 
7. Around the nation, local sheriffs and others have pushed back against new gun restrictions. “This is just a gun-grab measure,” said one New Mexico sheriff. https://www.nytimes.com/2019/03/11/us/state-gun-laws.html 
8. In the On Politics newsletter: What do the president’s recent trips to Japan, Britain and a Virginia church have in common? Flattery. https://www.nytimes.com/2019/06/03/us/politics/on-politics-with-lisa-lerer-trumps-day-of-prayer.html 
9. After Congress failed to pass legislation in the wake of the 2012 shooting, activists turned their energy toward building infrastructure for future fights. https://www.nytimes.com/2019/04/29/us/politics/newtown-parkland-guns.html 
10. The Parkland students became a force for gun control legislation and boosted the youth vote. Here’s how they changed America’s response to mass shootings. https://www.nytimes.com/2019/02/13/us/parkland-shooting.html 

**background support trump checks gun shooting bill universal young guns**
1. The F.B.I. also said it had opened a domestic terrorism investigation into the shooting at a Gilroy, Calif., garlic festival. https://www.nytimes.com/2019/08/06/us/mass-shootings.html 
2. New York Times reporters followed the exchanges and provided context around the candidates’ claims. https://www.nytimes.com/2019/07/30/us/politics/fact-check-democratic-debate.html 
3. A former governor of Colorado and mayor of Denver, Mr. Hickenlooper is running for president on a more centrist platform than many of his competitors. https://www.nytimes.com/2019/03/04/us/politics/2020-john-hickenlooper-on-the-issues.html 
4. The California senator has not always offered accurate defenses of her record or assessments of President Trump’s policies. https://www.nytimes.com/2019/06/08/us/politics/fact-check-kamala-harris.html 
5. While fighting for stricter gun laws, I was always told I didn’t understand. Maybe now I do. https://www.nytimes.com/2019/06/01/opinion/sunday/shooting-laws-guns.html 
6. One year later, what have we learned from the shooting at Marjory Stoneman Douglas High School? https://www.nytimes.com/2019/02/14/learning/learning-with-parkland-a-year-after-the-school-shooting-that-was-supposed-to-change-everything.html 
7. Mr. Ryan, an Ohio congressman, has outlined a campaign focused on appealing to the working-class Midwestern voters who flipped to President Trump in 2016. https://www.nytimes.com/2019/04/04/us/politics/tim-ryan-2020-issues.html 
8. Two students were in custody after the shooting at STEM School Highlands Ranch, near Denver. https://www.nytimes.com/2019/05/07/us/colorado-school-shooting.html 
9. As the gun rights group lavished pay and perks on its leaders and partners, fueling infighting, it increasingly relied on its own charity for funds. Tax experts have questions. https://www.nytimes.com/2019/05/14/us/nra-finances-executives-board-members.html 
10. Shifting the gun violence debate, Senate Majority Leader Mitch McConnell says he now wants to consider background checks and other bills, setting up a potentially pivotal moment when lawmakers return in the fall. https://www.nytimes.com/aponline/2019/08/08/us/politics/ap-us-mass-shootings-congress.html 

**schumer said universal pelosi background trump ms aides check comments**
1. The Democrats said that reports about Cindy Yang raised “serious counterintelligence concerns” about access to Mr. Trump’s Florida estate, as well as about campaign finance violations. https://www.nytimes.com/2019/03/18/us/politics/cindy-yang-trump.html 
2. You can credit social movements for that. https://www.nytimes.com/2019/08/08/opinion/the-squad-democrats.html 
3. In his State of the Union address, the president toggled between conciliation and confrontation, and demanded a wall on the nation’s southwestern border. https://www.nytimes.com/2019/02/05/us/politics/trump-state-of-the-union.html 
4. Some advisers worry that the president is giving oxygen to a fire that otherwise might burn out or at least be left to crackle in the background. https://www.nytimes.com/2019/05/24/us/politics/trump-impeachment-fight.html 
5. The shutdown has not only widened the divide between the Senate majority leader and the House speaker, but also imperiled prospects for passing major legislation when the impasse ends. https://www.nytimes.com/2019/01/20/us/politics/mcconnell-pelosi-government-shutdown.html 
6. The state’s elections in November will test the potency of gun rights as a voting issue. Democrats are looking to take power and enact gun control legislation next year. https://www.nytimes.com/2019/08/08/us/politics/virginia-gun-control-mass-shootings.html 
7. During the contentious meeting, the president made his case for a border wall and rejected Democrats’ proposals for reopening the government while the two sides ironed out their differences. https://www.nytimes.com/2019/01/02/us/politics/trump-congress-shutdown.html 
8. President Trump sought to go over the heads of Congress to enlist support for his border wall, raising the stakes of a conflict that has closed many federal agencies. https://www.nytimes.com/2019/01/08/us/politics/donald-trump-speech.html 
9. President Trump cast the proposal, which included $5.7 billion for a border barrier, as a compromise as he sought to shift pressure to Democrats to end the government shutdown. https://www.nytimes.com/2019/01/19/us/politics/trump-proposal-daca-wall.html 
10. How do you think our country is doing right now? Are we better off than we were a year ago? Why or why not? https://www.nytimes.com/2019/02/05/learning/how-would-you-describe-the-state-of-our-union.html 

**said trump people mental health problem forget politics want reshaping**
1. In the On Politics newsletter: The president’s attacks on four congresswomen, and the response by his base, gave a sense of his re-election campaign. https://www.nytimes.com/2019/07/18/us/politics/on-politics-send-her-back.html 
2. His studies of the use of drugs to treat disorders led many to consider him “the father of psychopharmacology.” https://www.nytimes.com/2019/08/16/science/donald-klein-dead.html 
3. U.S. President Donald Trump suggested on Friday he could persuade the powerful National Rifle Association lobby group to drop its strong opposition to gun restrictions after recent mass shootings that have reignited the gun control debate. https://www.nytimes.com/reuters/2019/08/09/us/09reuters-usa-shooting.html 
4. Who’s less popular than Elton John? https://www.nytimes.com/2019/08/14/opinion/trump.html 
5. A rash of suicides by police officers has shaken the New York Police Department, leading the commissioner to declare a mental health emergency and highlighting the problem of untreated depression among law enforcement officers nationwide. https://www.nytimes.com/aponline/2019/08/15/us/ap-us-police-suicides.html 
6. The president took sharp aim at opponents even as he visited two cities in mourning after horrific mass shootings in Ohio and Texas. https://www.nytimes.com/2019/08/07/us/politics/trump-el-paso-dayton-visits.html 
7. At the Democratic debates in a humid Motor City, it wasn’t just the candidates who were on display and clamoring for attention. https://www.nytimes.com/2019/07/31/us/politics/democratic-debates-detroit.html 
8. Here’s what you need to know. https://www.nytimes.com/2019/07/01/briefing/north-korea-hong-kong-nba.html 
9. The newest debate among the Democratic presidential candidates is whether accepting an invitation from Fox News is a Faustian bargain. https://www.nytimes.com/2019/05/16/us/politics/on-politics-fox-news.html 
10. Stop talking so much about the America that he’s destroying. Save your breath for the America you want to create. https://www.nytimes.com/2019/07/20/opinion/sunday/trump-squad-democrats-2020.html 

**president checks something republicans bipartisan democratic hill capitol hard pressure**
1. Whether the president’s support is real or another momentary reversal will determine if Congress passes the first new federal gun control measures in years. https://www.nytimes.com/2019/08/09/us/politics/gun-background-checks.html 
2. Rather than present tough choices and coherent ideas, they are mostly responding to his outrages with empty rhetoric. https://www.nytimes.com/2019/08/15/opinion/on-immigration-the-democrats-are-playing-into-trumps-hands.html 
3. With the clock ticking toward a potential debt default, federal budget negotiators are maneuvering to isolate the man seen as the common enemy: Mick Mulvaney. https://www.nytimes.com/2019/07/18/us/politics/budget-negotiators-mick-mulvaney.html 
4. The trickle of Democrats backing an impeachment inquiry is threatening to turn into a flood, but there are few signs the rising tide will sway House Democratic leaders. https://www.nytimes.com/2019/08/01/us/politics/impeachment-house-democrats-trump.html 
5. Nearly all of the 2020 Democratic candidates gave speeches at the annual event, and while many joked about the size of the field, most sought to contrast themselves with President Trump. https://www.nytimes.com/2019/08/09/us/politics/iowa-democrats-wing-ding-dinner.html 
6. Those in favor of amending the National Emergencies Act of 1976 remain determined to pursue bipartisan changes in legislation they view as a surrender of congressional power. https://www.nytimes.com/2019/03/16/us/politics/trump-veto-emergency-act.html 
7. Elaine Chao has boosted the profile of her family’s shipping company, which benefits from industrial policies in China that are roiling the Trump administration. https://www.nytimes.com/2019/06/02/us/politics/elaine-chao-china.html 
8. Republicans defected by the dozens, despite President Trump’s endorsement and pressure from key outside groups, and Democrats were left to get the deal passed. https://www.nytimes.com/2019/07/25/us/politics/budget-spending-deal.html 
9. On the surface, the annual Aipac conference looks relatively unchanged. But recent actions by President Trump and rising criticism of Israel on the left are taking a toll. https://www.nytimes.com/2019/03/23/us/politics/aipac-israel-trump-democrats.html 
10. The House-Senate conference committee that has three weeks to strike a border security deal is dominated by lawmakers experienced in bipartisan compromise. https://www.nytimes.com/2019/01/28/us/politics/trump-congress-border-wall.html 

**officials trump organization president gun rights statement group muscle internal**
1. The pattern is clear: Hate-filled manifestos posted on websites populated by white supremacists, followed by gun attacks against blacks, Jews, Muslims, or Latin American immigrants. https://www.nytimes.com/reuters/2019/08/09/us/09reuters-usa-shooting-internet.html 
2. This is what happens when our nation’s leader normalizes hate. https://www.nytimes.com/2019/08/06/opinion/el-paso-shooting-latino.html 
3. Fox News Channel host Tucker Carlson faced criticism Wednesday for declaring white supremacy "a hoax," the same day President Donald Trump visited El Paso, Texas, after a white gunman who had written an anti-Hispanic rant killed 22 people. https://www.nytimes.com/aponline/2019/08/07/us/ap-us-fox-news-carlson.html 
4. In a private White House meeting this month, President Abdel Fattah el-Sisi of Egypt urged President Trump to deem his opposition terrorists, officials said. https://www.nytimes.com/2019/04/30/us/politics/trump-muslim-brotherhood.html 
5. The State Department's internal watchdog has found significant evidence of leadership and management problems, including possible political retribution against career employees, in the bureau that deals with international organizations. https://www.nytimes.com/aponline/2019/08/15/us/politics/ap-us-united-states-state-department.html 
6. Even in deep blue New York, there are limits to trolling President Trump. https://www.nytimes.com/2019/08/15/nyregion/barack-obama-avenue.html 
7. With a push from President Donald Trump, Israel on Thursday barred two Muslim-American congresswomen from entering the country for a visit, an extraordinary step bringing the longtime U.S. ally into Trump's domestic fight against political rivals ... https://www.nytimes.com/aponline/2019/08/15/world/middleeast/ap-ml-israel-us-congress.html 
8. Critics and allies said President Trump’s relative disinterest in human rights and focus on economics have kept him from taking sides between China and the protesters. https://www.nytimes.com/2019/08/13/us/politics/hong-kong-trump.html 
9. New York Attorney General Letitia James’s investigation of the National Rifle Association now encompasses the group’s board. https://www.nytimes.com/2019/08/06/us/nra-board-subpoena-letitia-james.html 
10. More than half a century after Lyndon Johnson fell short on his attempt at gun control, new battles bring fresh roadblocks and dispute. https://www.nytimes.com/2019/08/06/us/gun-background-checks.html 

**trump senator republicans laws democrat legislative many house president lawmakers**
1. Robert Mueller sounded the alarm about threats to the nation’s democracy, but lawmakers keep playing politics. https://www.nytimes.com/2019/07/27/opinion/election-security-mueller-trump.html 
2. The Legislature is poised to pass a bill that would allow three congressional committees to seek the release of President Trump’s state tax returns. https://www.nytimes.com/2019/05/21/nyregion/trump-tax-return-bills-new-york.html 
3. After President Trump stopped short of a broad legislative response to the weekend’s massacres, lawmakers in both parties said Mr. McConnell held the key. https://www.nytimes.com/2019/08/05/us/politics/mitch-mcconnell-guns.html 
4. Attorney General William P. Barr pulled out of a Thursday hearing of the House Judiciary Committee, and he has left House lawmakers who are investigating the president fuming and calculating. https://www.nytimes.com/2019/05/02/us/politics/house-democrats-barr-mueller.html 
5. Congress has tools to override the president’s declaration, but opponents most likely do not have the votes to overcome a veto. https://www.nytimes.com/2019/02/14/us/politics/trump-congress-national-emergency.html 
6. President Trump had promised Republicans would replace the Affordable Care Act with a better, cheaper health law. Then the Senate majority leader told him that would not be happening. https://www.nytimes.com/2019/04/02/us/politics/obamacare-donald-trump.html 
7. As history has shown with the Watergate and Iran-contra scandals, such investigations can gain legitimacy only when members of the president’s own party support them. https://www.nytimes.com/2019/05/11/us/politics/trump-republicans-watergate.html 
8. Reaching a deal over a disaster relief package was threatened by the White House’s push for money for immigration law enforcement and assistance at the southwestern border. https://www.nytimes.com/2019/05/07/us/politics/disaster-relief-border-security.html 
9. Mr. McKean said he would join the Democratic Party and called President Trump’s behavior unacceptable. “If this is the new normal,” he said, “I want no part of it.” https://www.nytimes.com/2019/04/24/us/politics/andy-mckean-iowa-trump.html 
10. President Trump amplified his attacks against the lawmakers, and they responded by charging that he was pressing the agenda of white nationalists from the White House. https://www.nytimes.com/2019/07/15/us/politics/trump-go-back-tweet-racism.html 

**gun safety noted country many feinblatt looking group back white**
1. Both cities are grieving after mass shootings last weekend, and opinions are divided over whether his arrival will provide comfort or incite rancor. The mood in El Paso is particularly fraught. https://www.nytimes.com/2019/08/06/us/politics/trump-dayton-el-paso-shootings.html 
2. If the president did not originally inspire the gunman, he has brought into the mainstream polarizing ideas and people once consigned to the fringes of American society. https://www.nytimes.com/2019/08/04/us/politics/trump-mass-shootings.html 
3. The N.R.A. is dealing with inner turmoil, lawsuits and a newly empowered Democratic House. The president’s visit is being thought of as a needed pep talk. https://www.nytimes.com/2019/04/26/us/politics/trump-national-rifle-association.html 
4. While fighting for stricter gun laws, I was always told I didn’t understand. Maybe now I do. https://www.nytimes.com/2019/06/01/opinion/sunday/shooting-laws-guns.html 
5. Sri Lankans, angered by the government's inability to prevent the Easter Sunday terror attacks that killed more than 250 people, want a strongman back in power who can guarantee their safety and bring back economic growth. https://www.nytimes.com/reuters/2019/08/12/world/asia/12reuters-sri-lanka-gotabaya-analysis.html 
6. Tuesday: Have crowd-control measures at Disneyland worked too well? Also, a new publishing behemoth and the streaming TV boom. https://www.nytimes.com/2019/08/06/us/disney-earnings-theme-parks.html 
7. Protests and counterprotests have jolted a market in Indiana where activists now hand out buttons that say “Don’t Buy Veggies From Nazis.” https://www.nytimes.com/2019/08/18/us/indiana-farmers-market-white-supremacy.html 
8. The National Rifle Association is trying to defeat a provision in the new Violence Against Women Act that could deny firearms to abusive boyfriends. But Congress is changing. https://www.nytimes.com/2019/04/01/us/politics/nra-domestic-violence-congress.html 
9. What does it mean when a gun control advocate who lost a son to violence also becomes a gun owner who enjoys shooting? https://www.nytimes.com/2019/06/06/opinion/gun-laws.html 
10. After Congress failed to pass legislation in the wake of the 2012 shooting, activists turned their energy toward building infrastructure for future fights. https://www.nytimes.com/2019/04/29/us/politics/newtown-parkland-guns.html 

**trump gun shooting bedminster pushing senator advocates republican laws tougher**
1. That’s why, as president, I will push to ban them again. https://www.nytimes.com/2019/08/11/opinion/joe-biden-ban-assault-weapons.html 
2. More than half a century after Lyndon Johnson fell short on his attempt at gun control, new battles bring fresh roadblocks and dispute. https://www.nytimes.com/2019/08/06/us/gun-background-checks.html 
3. But with Republicans in charge of the Senate and President Trump in the White House, an assault weapons ban has little chance of being signed into law before 2021. https://www.nytimes.com/2019/08/12/us/politics/assault-weapons-ban.html 
4. Some criticism of the president’s stance on gun control and his relationship to the rise of white nationalism came from conservative outlets. https://www.nytimes.com/2019/08/05/business/media/trump-shooting-media-coverage.html 
5. It was a week of exaggeration and outright fiction for President Donald Trump as he confronted the aftermath of two mass shootings in Texas and Ohio. https://www.nytimes.com/aponline/2019/08/10/us/politics/ap-us-fact-check-week.html 
6. Playing defense, President Donald Trump made up facts in the aftermath of two mass shootings and as U.S. businesses braced for a potentially devastating trade war with China. https://www.nytimes.com/aponline/2019/08/12/us/politics/ap-us-fact-check-week.html 
7. It's not quite "Trump-McConnell 2020," but it might as well be. https://www.nytimes.com/aponline/2019/08/09/us/politics/ap-us-trump-mcconnell-.html 
8. As a Democratic politician in deep-red Montana, Steve Bullock has long searched for a middle ground on guns. Now a presidential candidate in a party pushing hard for new gun-control laws, he still is. https://www.nytimes.com/aponline/2019/08/17/us/politics/ap-us-election-2020-bullock-guns.html 
9. The president took sharp aim at opponents even as he visited two cities in mourning after horrific mass shootings in Ohio and Texas. https://www.nytimes.com/2019/08/07/us/politics/trump-el-paso-dayton-visits.html 
10. In the wake of the mass shootings in El Paso and Dayton, Democratic presidential candidates on Saturday emphasized the urgent need to confront gun violence in America. https://www.nytimes.com/2019/08/10/us/politics/elizabeth-warren-guns-2020-democrats.html 


More information to come...
