# Amazon_Vine_Analysis

## Overview

This project measures the bias of the Amazon Vine review program. Companies pay a fee to Amazon and provide products to Amazon Vine members in exchange for product reviews. Using AWS, PySpark, and Amazon reviews under the “Baby” category, this analysis measures the amount of bias in the review program, if any.

Tools used:
- AWS and RDS
- PgAdmin 4 - PostgreSQL database
- Google Colab and PySpark

## Results

Image 1: Raw dataframe used to answer the following questions:
![image](https://user-images.githubusercontent.com/78892035/123833462-5bd0a980-d8d4-11eb-91ce-87315f288997.png)

How many Vine reviews and non-Vine reviews are there?

- Of the total review count of 25,557, 463 of these are Vine reviews and 25,094 are non-Vine reviews. 

Total Vine reviews

![image](https://user-images.githubusercontent.com/78892035/123834041-fc26ce00-d8d4-11eb-9694-8dc241e74a9a.png)

Total non-Vine reviews

![image](https://user-images.githubusercontent.com/78892035/123834117-0f399e00-d8d5-11eb-9b5e-cdeee50cc63c.png)

How many Vine reviews were 5 stars? How many non-Vine reviews were 5 stars? 

- 5 Star reviews totaled 12,235, with Vine totaling 202 and non-Vine totaling 12,033.

![image](https://user-images.githubusercontent.com/78892035/123834789-cd5d2780-d8d5-11eb-8f6c-5f7c53dc7f13.png)

What percentage of Vine reviews were 5 stars? What percentage of non-Vine reviews were 5 stars?

- Of the total amount of Vine reviews, about 44% were 5 stars.
- Of the total amount of non-Vine reviews, about 48% were 5 stars.

![image](https://user-images.githubusercontent.com/78892035/123835394-773cb400-d8d6-11eb-855d-821f02f3afea.png)

## Summary

While there are significantly less reviewers from Vine compared to non-Vine, the ratio of 5 star ratings remains consistent with about 44% of Vine and 48% non-Vine giving 5 star reviews, or nearly half of each group. The non-Vine group actually rated higher than the Vine group more often, supporting that the current data set does not suggest a positive bias from reviews in the Vine program.

To further investigate this result, additional analysis should be performed across other Amazon categories, and then compared. Furthermore, we could look in to the opposite end of the spectrum for reviews and look for bias for leaving 1 star reviews.

