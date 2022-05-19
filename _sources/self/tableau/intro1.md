# Tableau Introduction

## What is Tableau?

Tableau is a powerful data visualization tool used in the Business Intelligence industry. It helps simplify raw data into an easily understandable format.

It is a lot easier to break down complex data with Tableau and generate valuable insights. These insights can then be used by companies to make data-driven decisions.

## Dataset Introduction

The data set we will be using in this tutorial is Kaggles Titanic Dataset. You can download from [here](https://github.com/ardhiraka/PFDS_sources/raw/master/titanic.xlsx).

There are 12 variables present in this data set. Here is an overview:

- PassengerId: Each passengers unique ID
- Pclass: The passenger class; 1st, 2nd and 3rd. The first was the upper class, and the third was the lower class.
- Name
- Sex
- Age
- SibSp: Number of siblings and/or spouses on board
- Parch: Number of parents and/or children on board
- Ticket: Ticket Number
- Fare
- Cabin
- Embarked: Port of embarkation
- Survived: Whether or not a passenger survived the Titanic. A value of 1 means the passenger survived, and a value of 0 means they did not.

For this data analysis, We will created a list of simple questions we can answer by visualizing the Titanic dataset:

- How many people survived the Titanic?
- Which gender was more likely to survive the Titanic?
- Did the class the passenger was in have any impact on their survival?
- Were younger people more likely to survive the Titanic?
- Were passengers who paid higher fares more likely to survive the Titanic?

## Download Tableau

Click on this [link](https://public.tableau.com/s/download) to download and install Tableau Public on your computer. Tableau Public is a free service that allows anyone to create interactive visualizations.

It is a free version of the Tableau Software that allows you to use most of the software functions. You can connect to CSV files, Excel spreadsheets, and text documents.

However, you will not be able to save your work locally on your computer. You will have to save and access it from Tableau Public.

## Tableau Approach

1. Question: what are we aiming to answer?
2. Exploration: what does our data support?
3. Design: how will our dashboard look?

## Basic Tableu Terminology

### Data Connector

When you first open Tableau, you will be prompted to connect to a data file or server. Typically, locally saved data files or extracts are used. In my experience, servers are used by large organizations to align data files to what is held in the company records. To connect a data file, select a file type, then:

- Connection: shows which data files have been uploaded
- Files: shows all the sheets from the file
- Note: if this is a data refresh, make sure to refresh all extracts on the worksheets

### Worksheets

Worksheets are where all the visualizations are built. Worksheets can be combined and published as Dashboards or Storyboards.

- Show Me: Tableau’s standard charts, they are highly customizable so a great place to draw inspiration from
- Data Pane: loads in all columns from the data
- Dimensions: qualitative columns, splits the data into groups
- Measures: quantitative columns, simple table calculations can be performed on them
- View Pane: where visualizations are built
- Pill: represents a column. Columns can be dragged an dropped from the data pane onto the view pane
- Card: represents a given aspect of the visual (ex, columns or rows). What you drop a card into, a pill must fall within it (a card can have multiple pills)
- Columns: when a pill is dragged and dropped into this card, it will show this column in a table format on the view pane (format can be changed using Show Me)
- Rows: when a pill is dragged and dropped into this card, it will show this row in a table format on the view pane (format can be changed using Show Me)
- Filters: allows you to filter the data. Pills can be dragged and dropped into the Filter Pane (right click on the filter and select Show Filter, it will appear on the right side of the screen). Filters can also be created using formulas
- Marks: data points found in the visualization. Used for visual formatting to adjust specific features (ex, colour, label, size)

## Connect to DataSource

![connect](https://miro.medium.com/max/299/0*AYSNcfli0-EuOhrT.png)

After your installation is complete, open Tableau Public. You will see a pane that looks like this on the left side of the window.

To connect to our data, click on Microsoft Excel. Then, find the Excel spreadsheet we just created and open it.

You will see a window that looks like this:

![loaded](https://miro.medium.com/max/700/0*YZVcx3TyiWqV603L.png)

## Data Analysis

To start analyzing the data, click on Sheet 1 at the bottom left corner of the screen.

You will see the following screen come up:

![sheet1](https://miro.medium.com/max/700/0*pQNGOATc6An4kTgZ.png)

Pay careful attention to the data pane (on the left side of the screen). You will see the different variable names.

![data](https://miro.medium.com/max/258/0*aBhufasoEknZF3V4.png)

There are two things you need to know about the way Tableau classifies variables:

### Data Type

Firstly, Tableau assigns each variable a data type — String, DateTime, Decimal, etc.

It is important to take a look at each variable and ensure that the data type is correct since it is possible for Tableau to get it wrong ( For example, Tableau could incorrectly classify a Datetime object as a String).

In this case, however, Tableau has seemed to have assigned the correct data type to each variable. We do not need to make any changes here.

### Measures and Dimensions

Tableau also classifies variables into **measures** and **dimensions**.

Measures are types of variables that can be aggregated, or used for mathematical operations.

Dimensions are fields that cannot be aggregated.

You can think of measures as continuous variables, and dimensions as discrete variables (refer to the first step of the tutorial if you dont remember the difference).

Lets take a look at the data pane again:

![data](https://miro.medium.com/max/258/0*aBhufasoEknZF3V4.png)

The variables at the top half of the pane, such as Cabin and Embarked are classified as **dimensions**.

Variables in the bottom half, such as Age and Fare are classified as **measures**.

It is possible for Tableau to incorrectly assign a variable as a dimension or a measure. In this case, there are two instances where Tableau has done so. We will need to re-define these variables.

We will take a look at the data set again to identify the incorrectly defined variables.

![data](https://miro.medium.com/max/700/0*batDNQLN8r963qHZ.png)

The variables **Pclass** and **Survived** were classified as measures or continuous variables.

However, these variables are discrete. Although they are numerical, they represent a category and not some sort of quantity.

For example, take a look at the variable *Survived*. A value of 1 indicates that a person survived the Titanic, and a value of 0 indicates they didnt. This is a categorical variable.

We need to change these incorrectly defined variables before we start visualizing the data.

To do this, you just have to drag and drop. Click on the incorrectly defined variable and drag it up to the **dimension** section of the pane.

Heres what it should look like when youre done:

![data](https://miro.medium.com/max/259/0*wSfovTMFlYU77VQO.png)

There are only four variables in the **measure** section, and everything else is classified as a dimension.

Now, we can start with the visualization process.

## Data Visualization

### Histograms

We will start by visualizing one variable. When visualizing the spread of one numeric variable in a data set, a histogram is used.

First, we will visualize the distribution of the variable *Age*.

In order to do so, we will first need to create bins or intervals of the age group:

![data](https://miro.medium.com/max/385/1*N4Mnc3znXmlja-rcP6frcQ.png)
![data](https://miro.medium.com/max/461/0*otKTpU2pIzB8XoQX.png)

Choose a bin size of 10, and click OK.

The variable **Age (bin)** should appear on your data pane:

![data](https://miro.medium.com/max/262/0*XYkZ3nz9Ubk-8Xum.png)

To visualize the age group we just created, drag the **Age (bin)** variable to the Columns pane at the top of the screen. Then, drag the **train(Count) OR worksheet(Count)** variable to the Rows pane:

![data](https://miro.medium.com/max/700/0*hMFxj_FIcaQqqqTo.png)

After you do this, you will see a histogram like the one below:

![data](https://miro.medium.com/max/700/0*lwIqz1trRqlNoYSq.png)

This is a good, clear visualization of the age distribution in our data set. However, it can be improved.

If you look closely, you will notice the value **Null** on the X-axis.

To remove the null values:

- Click on the drop-down near **Age (bin)**, and click on **Show Filter**.
- Untick the checkmark next to **Null**, and you will no longer see null values in your histogram

![data](https://miro.medium.com/max/621/0*avA3Sr26RPwMDMFp.png)

If you want to change the colors of the bins, drag the Age (bins) variable to the Color button in the Marks card:

![data](https://miro.medium.com/max/194/0*AAAqmcqZXuk26rPi.png)

Then, click on Color -> Edit Colors to choose a color palette:

![data](https://miro.medium.com/max/340/1*jDornhXnC3PeWrph9nNsSw.png)

Select a color you like, click on Assign Palette, and click OK. You will now have a histogram with the colors you chose:

![data](https://miro.medium.com/max/660/0*JCkHZM732dIE5nDc.png)

> Similarly, we can now visualize the variable **Fare**.

You can do it yourself this time for passenger fares. This time, use bin size of 30.

![data](https://miro.medium.com/max/700/0*gq9Avs3XgzQ_X1Bl.png)

### Count Plots

Similar to the histograms we created for the variables **Age**, and **Fare**, we can create count plots for categorical variables.

First, we will visualize the counts of the variable **Survived**.

> Note: Remove the variable Age (bin) from the Columns section and the marks card. You will have to do this each time you want to create a new visualization.

Just drag the variable **Survived** to the Columns section and the variable **train(Count)** to the Rows section.

Then, drag the variable **Survived** to the Color button in the Marks card, and choose a color palette:

![data](https://miro.medium.com/max/407/0*lIzFqgQkk_PStuZ5.png)

![data](https://miro.medium.com/max/194/0*KK5ZrRexb_KZe7BU.png)

Heres how the graph will look:

![data](https://miro.medium.com/max/449/0*zPuMWiwzQghIxSLf.png)

> Similarly, we can now visualize the variable **Pclass**.

Follow the same steps as before, and you should get a visualization that looks like this:

![data](https://miro.medium.com/max/568/0*2q1JhNU6SC1gkraH.png)

### Bar Chart

Were female passengers more likely to survive the Titanic than male passengers?

To answer this question, two variables — **Survived** and **Sex** need to be visualized in a count plot. Based on the type of insight you want to get, you can color this by either variable:

![data](https://miro.medium.com/max/580/0*F_DG9IlgzRZH43CB.png)

![data](https://miro.medium.com/max/195/0*Chg8H3jHfQ53cIkQ.png)

The resulting plot will be something like this:

![data](https://miro.medium.com/max/649/0*nWslgNTnWBGHd2fi.png)

By just looking at this graph, we can find a correlation — female passengers did seem more likely to survive the Titanic than male passengers.

### Tableau’s Marks Card

Before moving on to the next visualization, you need to know about an important feature of Tableau — the marks card.

![data](https://miro.medium.com/max/264/0*qIBx_urAVYDPMGMj.png)

Click on the **Show Me** button on the top right corner of the page, and you can find the marks card. Here, you can see different types of charts.

Tableau allows you to play around with different types of graphs to visualize the same data — there are bubble charts, tree maps, box plots, etc.

You can take a look at some of these, and spend some time creating different charts.

However, be careful when using these to visualize your data. Some of these graphs may look pretty but aren’t necessarily the best visualization practices.

Using charts that are too sophisticated may make it difficult for others to read and interpret, so proceed with caution.

### Stacked Chart

An alternative way to visualize the **Sex** and **Survived** variables above is to use a stacked chart.

![data](https://miro.medium.com/max/269/1*KeUjb3Xz0NEaIOnUXMwfHA.png)

Click on the card that looks like a stacked bar chart.

You should see a graph that looks like this. The bars for the variable **Sex** are no longer visualized side by side. Instead, they are stacked on top of each other.

![data](https://miro.medium.com/max/427/0*yxQLhrNGNlLMpqtJ.png)

### More Visualizations

Applying what we have learned above, we can create visualizations to find answers to the following data questions:

**Did the passenger class a person was in have any impact on whether they survived the Titanic?**

![data](https://miro.medium.com/max/700/0*XtK1bKmchQDb3-99.png)

It looks like passengers in the third class were far less likely to survive than passengers of any other class.

**Did the port the passenger embarked from have any impact on their survival?**

![data](https://miro.medium.com/max/700/0*ZZusXvWeKK5Ty76r.png)

There appears to be no apparent relationship between the variables **Embarked** and **Survived**.

**Were younger passengers more likely to survive the Titanic?**

Note: To answer this question, you can use the variable **Age** or **Age (Bin)**.

![data](https://miro.medium.com/max/700/0*ZQZAMpiE8ASBvzA-.png)

![data](https://miro.medium.com/max/700/0*FerdqYRA5vrxAUXT.png)

The age distribution of passengers who survived the Titanic is similar to the age distribution of passengers who didn’t. There seems to be little to no correlation between age and survival.

**Were passengers who paid higher fare prices more likely to survive the Titanic?**

![data](https://miro.medium.com/max/700/0*ulSZiQhflOxF4Mbc.png)

It can be observed that passengers who paid higher fare prices ($50 and above) have higher survival rates than passengers who bought cheaper tickets.

### Visualizing Multiple Variables

Tableau is a great tool to use when you need to visualize the relationship between more than two variables at once because there are just so many ways to do it.

To show you an example, I will visualize the relationship between the variables **Age**, **Sex**, and **Survived**.

![data](https://miro.medium.com/max/560/0*baP26uR1zfpxHGuA.png)

![data](https://miro.medium.com/max/196/0*or2Xau4vJThAxyGC.png)

![data](https://miro.medium.com/max/700/0*Se48RGxrlDFfgn4B.png)

There are many different ways you can do this, depending on the variable you want to stand out.

You can re-position the graph and try coloring different variables, and see what answers your data question best.

Sometimes, visualizing the same variables in many different ways can give you an entirely new perspective.

I will now visualize a few more variables to find the relationship between them, and you should try these on your own.

**Fare**, **Sex**, and **Survived**

![data](https://miro.medium.com/max/700/0*kxKt1ggEZNb6cnjg.png)

**Fare**, **Pclass**, **Survived**

![data](https://miro.medium.com/max/700/0*AZhwloj2JkC_BNuC.png)

**Age**, **Pclass**, **Survived**

![data](https://miro.medium.com/max/700/0*8jN4ivT9a47yC0Gu.png)

## Marks, Tooltips, and Annotations

Using marks, tooltips, and annotations can make it easier for people to read your graph.

However, you should use these wisely to avoid cluttering your graph with too much information.

### Tooltips

Tooltips are the details that appear when you hover your pointer over the visualization:

![data](https://miro.medium.com/max/470/1*TdGtFZ-onEDnJl8JBGt1oA.png)

You can choose to add information to your tooltip, without adding it to the visualization.

Re-create the survival count chart above. Then, all you need to do is drag the variable you want to add to the Tooltip button in the Marks card:

![data](https://miro.medium.com/max/197/0*C_2g-jnSFPEblGzR.png)

This way, every time someone hovers a pointer over your graph, they will be able to see this additional information:

![data](https://miro.medium.com/max/458/1*SPKEmQiv1Zwn7lcP4lofeg.png)

As you can see in the chart above, the tooltip has information on the passenger’s sex, which is not displayed in the graph.

> I would not recommend using tooltips this way. When visualizing categorical variables, it is always better to use a different hue or a separate column. I only created this to show you how you can use tooltips in the future.

### Annotations

It is possible to display the information you see on the tooltip as an annotation on your graph.

This way, you can call out a specific mark or point on your graph and get readers to see it easily.

This is especially useful when visualizing location data in a map because you get to annotate and draw attention to a particular area.

Here’s how to annotate your graph:

- Right-click on the histogram and click on Annotate -> Mark

![data](https://miro.medium.com/max/456/1*STETpzZjK6v-WdgWZnl3Xw.png)

- A screen like this will appear. You can choose to remove marks you don’t want, and click **OK**.

![data](https://miro.medium.com/max/560/0*nXpXMI4ziF08RI0z.png)

You will now see the annotation appear like this:

![data](https://miro.medium.com/max/640/0*0Goo_TvV22tJdfx-.png)
