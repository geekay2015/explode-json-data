# Explode the nested dictionaries(JSON Objects)


## Goals & Objective
1. implent a dictionary flattening function
2. Test it on general and edge test case
3. Add exception handling to faile it gracefully

## Use Case:-
How much wood would a woodchuck chuck if a woodchuck could chuck wood?

Our analysts want to answer this question in an objective way, so they've
gathered a lot of data about woodchucks that they intend to crunch through
with SQL.

The problem is that the data they got is in JSON, and a lot of it is
not flat.

## Input JSON dictionary: 

```json
{
    "name": "Cap'n Chuck",
    "aliases": ["Chuck Force 1", "Whistlepig"],
    "physical": {
        "height_in": 26,
        "weight_lb": 18
    },
    "wood_chucked_lbs": 2281
}
```

## Expected output

```json
{
    "name": "Cap'n Chuck",
    "aliases.0": "Chuck Force 1",
    "aliases.1": "Whistlepig",
    "physical.height_in": 26,
    "physical.weight_lb": 18,
    "wood_chucked_lbs": 2281
}
```
## Environment used
1. Python 3.6.0 |Anaconda 4.3.0 (x86_64)
2. Pycharm IDE
3. Packages used - json, Unittest, pprint

## Code Structure
1. `flatten.py` -  Flatten function to explode the input dictionary
2. `test_cases_flatten.py` - test case to test the flatten function
3. Program Output 
```
{'aliases.0': 'Chuck Force 1',
 'aliases.1': 'Whistlepig',
 'name': "Cap'n Chuck",
 'physical.height_in': 26,
 'physical.weight_lb': 18,
 'wood_chucked_lbs': 2281}
 ````

## Follow-up Email
Semi-structured data formats such as JSON, Avro, and others have become the de facto form in which this data is sent and stored. Semi-structured data is easy for these applications to create and capable of representing a wide array of information.

Two of the key attributes that distinguish semistructured data from structured data are 
- the lack of a fixed schema and nested data structures. Whereas structured data requires a fixed schema defined in advance. semi-structured data does not require a prior definition of a schema and can constantly evolve new attributes can be added at any time. 
- Also unlike structured data, which represents data in a flat table, semi-structured data can contain hierarchies of nested
information.

The flexibility of schemaless design and the ability to represent a wide range of information are key reasons that semi-structured data has become so widely used. New and richer information can easily be added to the data at any time.

However, the flexibility and expressiveness of schemaless design create challenges when the data needs to be analyzed. As the use of semi-structured data formats has increased, so has the need to analyze that data. Although a limited amount of analysis can be done on semi-structured data in isolation, the most valuable insights come from bringing semi-structured data together with other data, particularly structured relational data. 

Relational databases were not designed to store and process semi-structured data. They were architected based on the assumption that a static schema could be determined in advance. That design assumption has made possible a wide array of optimizations—pruning, predicate push-down, and others—but at the cost of sacrificing the flexibility that schema-on-read offers.

## Do you see any potential problems with the approach they're taking? 
1. The current approach needs to transform semi-structured data into a fixed schema before loading it into the data warehouse.
2. This approach creates a very fragile data pipeline that requires significant maintenance. Every change in the data—adding a new attribute, eliminating an attribute or adding a new level of nested information—breaks the data pipeline such that information is lost until the transformation and attribute extraction is updated to handle the new data structure.

## Is there an alternative way of tackling the problem that they should consider?
To handel semistructured data efficiently you need the following:
- Flexible-schema datatype: load semistructured data without much transformation
- Storage optimization: transparently converted to optimized internal storage format
- Query optimization: for fast and efficient SQL querying

we can get the above With a combination of Aapche Spark + NoSQL database on cloud.
1. **NoSQL data platform** to store and analyze semi-structured data. Systems such as Hadoop can adapt to the rapid evolution in semistructured data because they can store that data without requiring definition of a fixed schema. 
2. **Apache Spark** can be use for high-performance querying, particularly querying that combines semi-structured and
structured data. Spark SQL provides a natural syntax for querying JSON data along with automatic inference of JSON schemas for both reading and writing data. Spark SQL understands the nested fields in JSON data and allows users to directly access these fields without any explicit transformations.
