# Mindful Money Technical Challenge

**Due date:** 5pm Monday 11 April

**Expected time commitment:** 1.5 - 3 hours

This challenge is a simplified subset of Mindful Money’s data processing pipeline. The high level goal is to be able to inform the public in a clear, easy-to-understand way about how much an investment fund is invested in certain harmful industries.

## Background

Every 6 months, all investment funds that operate in New Zealand must disclose their holdings (companies that they invest in) to the MBIE. Mindful Money takes these lists of holdings for each fund, and checks how many of these companies are involved in harmful industries.

Take fossil fuels, for example. [Sustainalytics](https://www.sustainalytics.com/) is a third party provider of data about companies’ ethical standards. We export a list of all the companies in the world that are involved in fossil fuels via their UI console. Let’s call this list “ff_comps” (short for “fossil fuel companies”). We then compare the names on “ff_comps” to the companies that New Zealand funds invest in, to figure out what % of each fund is invested in fossil fuels.

## Problem

**The problem is that the names in the Sustainalytics system do not always match up to the names in the MBIE system.** Your challenge is to come up with a way to match up these names, and provide insights about which funds are the most ethical based on their involvement in fossil fuels.

## Data provided

You can find the following mock data for this challenge in [this Google Drive folder](https://drive.google.com/drive/folders/1la2rdcefiNnQv-28vont1pyChIy3cXbQ?usp=sharing):
- **mbie_fund_holdings.json:** A nested JSON file of fund holdings from MBIE
- **ff_comps.csv:** A CSV list of fossil fuel company names from Sustainalytics
- **ff_names_matched.csv:** A CSV list of fossil fuel company names from Sustainalytics, matched to their names in MBIE (for testing purposes)

## Tasks

1. **Building an MVP model in Python (max. 1.5 hours):** Match the fossil fuel company names in **ff_comps.csv** to the “holding” field in the **mbie_fund_holdings.json** dataset.
    - We recommend that you first look through the data to see what it looks like. You’ll notice that the company names sometimes don’t match across the two datasets exactly. E.g. “Adani Power Limited” vs. “Adani Power Ltd”
    - You’ll need to use some kind of model or set of heuristics to compare the two lists for matches.
    - **We are not assessing you on the complexity or sophistication of your model.** Accuracy is not the most important thing here - in fact, it doesn’t even have to be particularly good. We’re mostly looking at how you approach the problem, and how you go about implementing an MVP that can be later iterated on. It can be a really, really simple “model”. We recommend timeboxing yourself to 1.5 hours max.
    - It’s fine to use third party libraries, off the shelf models, whatever you wish.
    - We’ve given you a labelled dataset, **ff_names_matched.csv**, for your convenience in case it’s helpful (but you don’t have to use this).
    - You may also need to do some data wrangling on the nested JSON.
    - Note: please take the `mbie_fund_holdings.json` data as containing complete information about each fund's holdings, and you don't need any further information (e.g. googling for Netflix's direct/indirect investment in fossil fuels) to answer the question. We just made up the names of a bunch of companies, using recognisable names like Netflix for some, and made up ones for others. You can basically just sum the amounts for fossil fuel companies listed in `ff_comps.csv` per fund, and then divide by the total sum of amounts for each fund.
2. **Using the model (5-10 mins):** Use the model to calculate the % of each fund’s money that is invested in fossil fuels (use the “amount” value).
3. **Future work (5-10 mins):** Write a high-level plan for what else you would do to improve this data processing pipeline. (max. 200 words, bullet points preferred). Remember that the end user is Mindful Money volunteers, who must repeat this process every 6 months.
4. **Data visualisation (15-30 mins):** Design and implement a data visualisation using any tools or languages that helps the general public make an informed decision on which fund to invest in.
    - You can use any kind of data visualisation you wish. Just keep in mind that the audience is a random person on the internet who probably has a very short attention span, and very little knowledge about investment or data. How can you ensure that the information is most effectively communicated?

## Assessment criteria
Your solution will be evaluated against the following criteria:
1. We can easily run your code/notebook to view the results & data visualisations.
2. A reasonable MVP approach for matching company names has been chosen.
3. Code is written in a way that’s clean, maintainable, and performant.
4. Answers are organised and presented clearly.
5. The data visualisation is easy to understand, accurate, and designed with the end user in mind.

## What we aren’t assessing

- The way you use version control (how you commit code to git, etc.).
- Starting from scratch vs. using existing tools - you can use any libraries (e.g. pandas), templates, or code snippets that you find online.

## Submission

You can submit your code, data visualisations, and insights, in any one of the following ways:
1. Public GitHub/GitLab/BitBucket repository: just email us the link to it at liam@mindfulmoney.nz
2. Private GitHub repository: Add [LMilbank](https://github.com/LMilbank) as a collaborator so that we can access it, and send an email to liam@mindfulmoney.nz letting him know that you’ve done that.
3. Email: zip up all the data/code/notebooks required to produce your results + any images/figures/comments and email it to liam@mindfulmoney.nz

## Reach out if you have questions

- We’re all humans so if you need more time or life stuff crops up, please reach out and let us know. We are more than happy to accommodate your needs.
- If you’d like something clarified - feel free to ask! Not everyone interprets things the same way and we’d be happy to discuss it with you.
