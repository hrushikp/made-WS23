# Project Plan

## Title
<!-- Give your project a short title. -->
IMDB Movie Analysis for MADE

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Does writing an example question help students write better project plans?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
XY is an important problem, because... This projects analyzes XY, using method A. The results can give insights into...

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: ExampleSource
* Data URL: https://datasets.imdbws.com/
* Data Type: TSV

Imdb database with data of
*tconst (string) - alphanumeric unique identifier of the title
*titleType (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)
*primaryTitle (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release
*originalTitle (string) - original title, in the original language
*isAdult (boolean) - 0: non-adult title; 1: adult title
*startYear (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year
*endYear (YYYY) – TV Series end year. ‘\N’ for all other title types
*runtimeMinutes – primary runtime of the title, in minutes
*genres (string array) – includes up to three genres associated with the title

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Example Issue [#1][i1]
2. ...

[i1]: https://github.com/jvalue/made-template/issues/1
