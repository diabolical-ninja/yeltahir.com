---
title: "Epidemic Modelling"
date: 2020-10-09T00:00:00+11:00
draft: false

resources:
- name: featured-image
  src: topredictane.jpg

toc:
  auto: false
math:
  enable: true
---


As the coronavirus pandemic continues to spread throughout 2020 and the world, I find myself somewhat charmed to see the mathematics studied back in my university days make the news and can't help but reminisce. As such I decided to dust off the text books and reacquaint myself with modelling an epidemic. On y va!


## What is a compartmental model?

The basis for many (most?) epidemic models is compartmental modelling. These allow different states to be captured in distinct compartments and the effects of moving between each comparement observed. The simplest model used is what is known as the SIR model, which stands for Susceptible - Infected - Recovered.

The premise is, at anypoint in time an individual can be:
* Susectible to being infected
* Infected & thus infectious
* Recovered (or removed) and no longer available to be infected

Over time individuals can move through each compartment and thus we have the basis for our compartmental model:

{{< mermaid >}}
graph LR;
    Susceptible --> Infected
    Infected --> Recovered
{{< /mermaid >}}

Futhermore, we can define the rate at which people move from compartment to compartment. Normally these are defined as:
- $\beta$: The probability of a susceptible individual becoming infected upon interaction with an infected party
- $\gamma$: The rate at which infected individuals recover, also known as the recovery rate

{{< mermaid >}}
graph LR;
    Susceptible --Beta--> Infected
    Infected --Gamma--> Recovered
{{< /mermaid >}}

With this we can to build our model. Noting that the number of individuals in each compartment changes over time, we now have:

- $ S(t) $ : The number of susceptible individuals at time $t$    
- $ I(t) $ : The number of infected individuals at time $t$    
- $ R(t) $ : The number of recovered individuals at time $t$    


Like every good mathematical model, lets add in some assumptions to make our life a little easier. Firstly, lets assume that the population remians static over time, thus:

$$ S(t) + I(t) + R(t) = N $$

And to make things even easier, lets represent it as proportions of the population rather than absolute counts:

$$ S(t) + I(t) + R(t) = 1 $$

That's a good start, but what we really want to know is how people move between compartments and how the values for $\beta$ and $\gamma$ impact the outcome of an epidemic.


## Moving compartments

### Getting Infected
At any point in time the number of people getting infected is defined as the proportion that are susceptible, interacting with the infectious group and getting infected at a rate of $\beta$, thus we get $\beta \times S(t) \times I(t)$.

### Recovering
Furthermore, at any point in time infectious people are recovering giving us $\gamma \times I(t)$

### Putting it all together
As the indidivuals getting infected and recovering are moving between groups, they allow us to define the rate of change for the population in each compartment, giving us:

$$ \frac{dS}{dt} = - \beta S(t) I(t) $$
$$ \frac{dI}{dt} = \beta S(t) I(t) - \gamma I(t) $$
$$ \frac{dR}{dt} =  \gamma I(t) $$


We now have the classic SIR model. So, what can we do with it?


## What does SIR tell us?

Before we get started, we need....

### Some more assumptions

At $t=0$ there has to be at least 1 infected individual otherwise there is no epidemic. Also, again to make the maths a little easier, we're going to assume that everyone else is suspectible. 

$$ S(0) \approx 1 $$
$$ I(0) > 0,  I(0) \approx 0$$
$$ R(0) = 0 $$


### The rate of infection

Furthermore, at the start of an epidemic we need the number of people getting infected to be growing and thus have:

$$ \frac{dI}{dt} > 0 $$

Additionally, can rearrange the equation to get:

$$ \frac{dI}{dt} = I(\beta S(t) - \gamma) $$


In order to satisfy a positive growth in the beginning we need:

$$ \beta S(t) - \gamma > 0 $$

Given our prior assumption of $ S(0) \approx 1 $ and with some more rearranging we get:

$$ \frac{\beta}{\gamma} > 1 $$ 

In other words, for an epidemic to take-off we need the rate of people getting infected to exceed the rate of recovery. This is commonly referred to as the **basic reproductive ratio** and defined as:



{{< admonition type=quote title="The Basic Reproductive Ratio" open=true >}}
$$ \frac{\beta}{\gamma} = R_0 > 1 $$ 

The average number of secondary cases arising from an average primary case in an entirely susceptible population
{{< /admonition >}}


This seemingly simple number is key because it informs how fast an indectious disease grows and provides a basis to try and control it. In order to stop the spread of an epidemic, one must ensure people recover faster than new individuals are infected and through emperical calculation of the effective $R_0$ governments and policy makers can assess whether or not their measures are working.



### How bad will it be?

Now we know how fast it will spread and how to control it, lets see if we can identify how big the epidemic will be.




## This model is too simple, what about in real life?

Now obviously we've made some assumptions along the way, sanded off a few corners to make modelling a little easier but what about in real life where the corners are rough, people don't behave exactly as planned and governments can make policy decisions to interfere with the spread of the disease?

This is where the compartmental model becomes a really powerful tool. By following the same reasoning as with SIR we can introduce as many compartments as we like with different rates of movement, interractions and probabalistic behaviours.

<!-- Examples for isolation &/or vaccination -->


## References

For those interested in the modelling used by the Australian government to inform the original COVID19 response, the Doherty Institute [released their research](https://www.doherty.edu.au/uploads/content_doc/McVernon_Modelling_COVID-19_07Apr1_with_appendix.pdf) and you can see this approach to modelling at work, albiet with a tad more complexity.

- [Assessing the risk of spread of COVID-19 to the Asia Pacificregion](https://www.doherty.edu.au/uploads/content_doc/Geard_importation_risk_assessment_COVID19_Apr7.pdf)
- [Estimating the case detection rate and temporal variation in transmission of COVID-19 in Australia Technical Report 14th April 2020](https://www.doherty.edu.au/uploads/content_doc/Estimating_changes_in_the_transmission_of_COVID-19_April14-public-release.pdf)



The book [Modeling Infectious Diseases in Humans and Animals](https://press.princeton.edu/books/hardcover/9780691116174/modeling-infectious-diseases-in-humans-and-animals) by Matt J. Keeling and Pejman Rohani is an excellent read and great introduction to mathematical modelling of diseases, covering compartmental models discussed here and its many variations.




