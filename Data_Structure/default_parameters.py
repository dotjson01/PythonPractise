def clean_name(first_name, last_name, country='n/a'):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first+ " " + last
    print(full_name, "From", country)


# default parameters
clean_name("mohan","kumari","bihar")