import sys
bins = {
        'loan_amnt':[
            {
            "label": "(-inf, 1000)",
            "max": 1000
           },
            {
                "label": "(1000, 10000)",
                "max": 10_000
            },
            {
                "label": "(10_000, 20_000 )",
                "max": 20_000
            },
            {
                "label": "(20_000, inf)",
                "max": sys.maxsize
            },
        ],
        'int_rate':[
                    {
                "label": "(-inf, 9)",
                "max": 9
            },
            {
                "label": "(9, 15)",
                "max": 15
            },
            {
                "label": "(15, 20)",
                "max": 20
            },
            {
                "label": "(20, inf)",
                "max": sys.maxsize
            },
        ],
        'annual_inc': [ 
                {
            "label": "(-inf, 3.000e+03)",
            "max": 3.000e+03
            },
            {
                "label": "(3.000e+03, 6.0000e+04)",
                "max": 6.0000e+04
            },
            {
                "label": "(6.0000e+04, 1.00000e+04)",
                "max": 1.00000e+04
            },
            {
                "label": "(1.00000e+04, 1.0000e+05)",
                "max": 1.0000e+05
            },
            {
                "label": "(1.0000e+05, inf)",
                "max": sys.maxsize
            },
        ], 
        'dti' : [ 
            {
            "label": "(-inf, 10)",
            "max": 10
            },
            {
                "label": "(10, 20)",
                "max": 20
            },
            {
                "label": "(20, 30)",
                "max": 30
            },
            {
                "label": "(30, inf)",
                "max": sys.maxsize
            },
        ],
       'delinq_2yrs': [ 
            {
            "label": "(-inf, 10)",
            "max": 10
            },
            {
                "label": "(10, 20)",
                "max": 20
            },
            {
                "label": "(20, inf)",
                "max": sys.maxsize
            },
       ], 
       'inq_last_6mths':[
            {
            "label": "(-inf, 10)",
            "max": 10
            },
            {
                "label": "(10, 20)",
                "max": 20
            },
            {
                "label": "(20, inf)",
                "max": sys.maxsize
            },
            
       ], 
       'open_acc':[
            {
            "label": "(-inf, 20)",
            "max": 20
            },
            {
                "label": "(20, 40)",
                "max": 40
            },
            {
                "label": "(40, 60)",
                "max": 60
            },
            {
                "label": "(60, inf)",
                "max": sys.maxsize
            },
       ], 
    #    'pub_rec':[
    #         {
    #         "label": "(-inf, 1)",
    #         "max": 30
    #         },
    #         {
    #             "label": "(1, inf)",
    #             "max": sys.maxsize
    #         }
    #    ], 
       'revol_util':[
             {
            "label": "(-inf, 50)",
            "max": 50
            },
            {
                "label": "(50, 100)",
                "max": 100
            },
            {
                "label": "(100, 250)",
                "max": 250
            },
            {
                "label": "(258, inf)",
                "max": sys.maxsize
            },
       ],
       'total_acc':[
            {
            "label": "(-inf, 20)",
            "max": 20
            },
            {
                "label": "(20, 50)",
                "max": 50
            },
            {
                "label": "(50, 100)",
                "max": 100
            },
            {
                "label": "(100, inf)",
                "max": sys.maxsize
            },
       ], 
       'out_prncp':[
            {
            "label": "(-inf, 1000)",
            "max": 1000
            },
            {
                "label": "(1000, 10_000)",
                "max": 10_000
            },
            {
                "label": "(10_000, 30_000)",
                "max": 30_000
            },
            {
                "label": "(30_000, inf)",
                "max": sys.maxsize
            },
       ], 
       'total_pymnt':[
            {
            "label": "(-inf, 1000)",
            "max": 1000
            },
            {
                "label": "(1000, 15_000)",
                "max": 10_000
            },
            {
                "label": "(15_000, 35_000)",
                "max": 30_000
            },
            {
                "label": "(35_000, inf)",
                "max": sys.maxsize
            },
       ],
       'total_rec_int':[
            {
            "label": "(-inf, 1000)",
            "max": 1000
            },
            {
                "label": "(1000, 10_000)",
                "max": 10_000
            },
            {
                "label": "(10_000, 20_000)",
                "max": 30_000
            },
            {
                "label": "(20_000, inf)",
                "max": sys.maxsize
            },
       ]

}




