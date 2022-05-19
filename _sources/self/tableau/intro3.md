# Tableau Dashboard Practice

## Dataset Introduction

The data set we will be using in this tutorial is Superstore Sample from Tableu Public Dataset. You can download from [here](https://github.com/ardhiraka/PFDS_sources/raw/master/sample-data.xlsx).

Based on the dataset, our goal is to build a dynamic dashboard. From the dashboard, a viewer should be able to learn the following insights:

- Top-level revenue, profit, profit ratio and units sold for the year.
- YoY (Year-Over-Year) performance by customer segment (customer segment refers to Corporate, Consumer, Home Office).
- View sub-category performance by the active metric (from revenue, profit, profit ratio and units sold).
- Best performing sub-categories within each customer segment for the chosen metric.

In total, there are four main steps to build this dashboard:

- First, format the top-level KPIs as BANs in Tableau.
- Then, visualize the YoY customer segment performance with a line plot.
- Then, visualize the YoY sub-category performance under each customer segment with a bar plot.
- Finally, define the metric and year user selection dropdowns.

## Visualization

### KPIs

Creating a BANs for the main KPIs such as profit, revenue, avg profit ratio and units sold, is always a good way to present your insights to a viewer who doesn’t know very much details of the dataset.

![BANs](https://miro.medium.com/max/630/1*YjutLebg9E3iygKfIyV9IA.gif)

In the first part, We chose the KPIs that I want to include in my BANs first. Then, We dragged each of the measures to the Label in the Marks section.

By default, Tableau assumes the aggregation is a sum of the measure. However, for the profit ratio, we would like to calculate the average instead of the sum. You could change it to average by right click on the aggregated measure in the Marks section.

![BANs](https://miro.medium.com/max/630/1*j-sd6j58XKS0g-4fCa0fbg.gif)

In the second part, We created a Year filter by right click on the Year and select Show Filters. Then, by left clicking on the Text in the Marks section and selecting the three dots, we could change the font, size and color of the body text in the BANs.

![BANs](https://miro.medium.com/max/630/1*IYdwX33iRb0QCR6MVeI5kA.gif)

Now, we have completed the KPIs section but you may find that a year filter is not the best way to control in the visualization. For example, if we have multiple sheets and each of them contains a year filter then the final dashboard would look very messy. Therefore, in the final section of the article, I will show you how to add custom selection dropdowns in Tableau by creating new parameters and calculated fields.

### YoY Segment Performance

Besides the previous top-level insights, a viewer may want to have a further look into the YoY performance under each segment.

We will creating a line plot that meets the requirement.

![BANs](https://miro.medium.com/max/630/1*VJeTWeCu2fR2pHkIEWcTBg.gif)

You could also edit the color of the line plot by left clicking on the arrow of the SUM(Profit).

Back to the dashboard requirement, a viewer should also be able to see the performance by an active metric (from revenue, profit, profit ratio and units sold). As mentioned at the end of the KPIs section, we will create the active metric & year selection dropdowns in the final part of the article.

### YoY Sub-category Performance

In this step, We will use bar plot to show the YoY sub-category level performance for each segment under the selected metric Profit.

![BANs](https://miro.medium.com/max/630/1*zg6-K502QFljLipFaRWW5g.gif)

Also, you could edit the bar plot color by clicking on the aggregated measure and select Edit Colors.

As you may find, in this graph, the year filter appears again and it already appeared in the previous two graphs. It’s not necessary to keep all three year filters for each graph in the final dashboard.

So now I will introduce how to build and connect the user selection dropdowns for both the year & metric (from revenue, profit, profit ratio and units sold) filters.

### User Selection

![BANs](https://miro.medium.com/max/403/1*-AeG9YrLkvCpsPJYDq_OEQ.png)

The dropdowns we want to achieve will look like above in the final data dashboard. Two selection dropdowns, one is for the active metric and one is for the selected year.

Starting from the KPIs, we need to define the Select Year as a new parameter and Chosen Year as a new calculated field.

![BANs](https://miro.medium.com/max/630/1*OK_gpUK7Z8MEbNs0YCiRgQ.gif)

Since you can use the newly created parameter and calculated field in the other sheets, you could simply replace any year variables in your graph with the new Chosen Year and repeat the Show Parameter step. It should work well for the other two sheets as well.

Finally, we are creating the Select Metric, it’s actually easier than the Select Year.

![BANs](https://miro.medium.com/max/630/1*37JTkjlj_XdW3-8AYThYaA.gif)

Similar to the Select Year, the Select Metric parameter and the Chosen Measure calculated field can be found on the other sheets. Some differenece are the data types and the formulas within each filter.

Finally, to create a dashboard and adjust its layout, simply click the New Dashboard icon, drag the sheets you need and move them as your design.

My final dashboard looks like the following:

![BANs](https://miro.medium.com/max/630/1*io2VIkqgiWPdTXoH9yFjbA.png)
