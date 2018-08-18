# Explode the nested dictionries using

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

For example:

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

## Project Structure
1. `explode_jsond_data.py` -  Flatten function
2. `test_cases_explode_json.py` - test case to test the flatten function


## Follow-up Email

Team Woodchuck is ready to charge ahead and build their first analytics
product on this basic architecture. Do you see any potential problems with
the approach they're taking? Is there an alternative way of tackling the
problem that they should consider?

Write a brief email to the team laying out your thoughts. You can edit it
in here.

## Feedback

When you're done with everything, answer the following questions. We use
this feedback to tune the exercise and give you an opportunity to add any
extra thoughts you may have.

You can edit your answers in here.

1. How long did the programming exercise take you to complete? How about
   the email?
2. Any comments on the whole exercise process itself, or on any of your
   answers?
