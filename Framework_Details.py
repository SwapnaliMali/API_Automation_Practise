"""
What is a Framework ?
Frameword is a structure, skeleton,guidelines,best practise to create a structure. Code to be maintained, reused & scaled.

Frameworks types -
1. Data driven --> When u inject multiple / huge data from external sources(excel, csv, json etc.) to ur test scripts
   then it is called Data driven testing. here same repetative column data is taken with different row data.

2. Module Driven --> Here for each feature different modules are created. Ex - create booking(test_create_booking),
   delete booking, update booking each has it different, drawback ->  it has repetative data a lot like url, json payload,headers etc.
   Make request & verify request.

3. Hybrid framework --> Here it is a combination of Data Driven + Module Driven framework, it is done so as to avoid the drawbacks of
   both frameworks.

We will be using here custom hybrid framework with following qualities -->
1. Seperate folder for generic code
2. Utilites - getting date, Using FakerJs, ReadCSV, ReadingExcel
3. Verification logic or code -> Generic code

This is further classified into 2 folders as SRC & tests but SRC is not recommended, only tests should be used.

Further it has - Helpers, Resources(csv file),Utils(fakerjs,csv read),Constants( url, verification logic)




"""