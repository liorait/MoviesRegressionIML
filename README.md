# MoviesRegressionIML
A machine learning project in IML course

Files list:
------------

regression :
------------
our main model train, predict and plot
    functions:
    
    load_data(pathname)
    preprocess(X)
    our_train_test_split(X, y)
    split_X_y(X)
    train(X, y)
    predict(X)
    error_rate(y, y_hat)

preprocessing :
-------------
pre-process the data into all numbers matrix
    function:
    process_begin(data) - main function, call to others

    remove(data, feature)
    add_value_to_cast(data)
    add_value_to_crew(data)
    calculate_crew_value(crew_dict)
    calculate_crew_average(data)
    calculate_cast_average(data)
    genre(data)
    original_language(data)
    belongs_to_collection(data)
    cast_process(data)
    crew_process(data)
    process_nan(data)
    release_date(data)
