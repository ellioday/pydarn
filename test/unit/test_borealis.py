# Copyright 2019 SuperDARN Canada, University of Saskatchewan
# Author: Marci Detwiller
"""
This test suite is to test the implementation for the following classes:
    BorealisSiteRead
    BorealisUtilities
    BorealisSiteWrite
Support for the following Borealis file types:
    rawrf
    antennas_iq
    bfiq
    rawacf
And supports conversion to the following Borealis types:
    bfiq -> iqdat
    rawacf -> rawacf
"""
import bz2
import collections
import copy
import filecmp
import logging
import numpy as np
import os
import random
import unittest

from collections import OrderedDict

import borealis_rawacf_data_sets
import borealis_bfiq_data_sets
import pydarn

pydarn_logger = logging.getLogger('pydarn')

# Site Test files
borealis_site_bfiq_file = "../test_files/20190909.2200.02.sas.0.bfiq.hdf5.site"
borealis_site_rawacf_file = "../test_files/20190909.2200.02.sas.0.rawacf.hdf5.site"
borealis_site_antennas_iq_file = "../test_files/20190909.2200.02.sas.0.antennas_iq.hdf5.site"
# borealis_site_rawrf_file =

# Array Test files
borealis_array_bfiq_file = "../test_files/20190909.2200.02.sas.0.bfiq.hdf5"
borealis_array_rawacf_file = "../test_files/20190909.2200.02.sas.0.rawacf.hdf5"
borealis_array_antennas_iq_file = "../test_files/20190909.2200.02.sas.0.antennas_iq.hdf5"

# Problem files
borealis_site_extra_field_file = '../test_files/20190402.1731.12.sas.0.bfiq.hdf5' # timestamp_of_write
borealis_site_missing_field_file = ""
borealis_site_incorrect_data_format_file = ""

borealis_array_extra_field_file = ""
borealis_array_missing_field_file = ""
borealis_array_incorrect_data_format_file = ""
borealis_array_num_records_error_file = ""
borealis_empty_file = '../test_files/empty.rawacf'


class TestBorealisFunctions(unittest.TestCase):
    """
    Testing class for functions from within borealis.py
    """

    def test_read_borealis_file_bfiq(self):
        print('Reading site file as records:')
        record_data = pydarn.read_borealis_file(borealis_site_bfiq_file, 'bfiq', site=True, records=True)
        self.assertIsInstance(record_data, dict)
        random_key = random.choice(list(record_data.keys()))
        print(record_data[random_key])
        print('Read site file as records.')

        print('Reading site file as arrays:')
        array_data = pydarn.read_borealis_file(borealis_site_bfiq_file, 'bfiq', site=True)
        self.assertIsInstance(array_data, dict)
        print(array_data['pulses'])
        print('Read site file as arrays.')

        print('Reading arrays file as arrays:')
        array_data = pydarn.read_borealis_file(borealis_array_bfiq_file, 'bfiq')
        self.assertIsInstance(array_data, dict)
        print(array_data['pulses'])
        print('Read arrays file as arrays.')

        print('Reading arrays file as records:')
        record_data = pydarn.read_borealis_file(borealis_array_bfiq_file, 'bfiq', records=True)
        self.assertIsInstance(record_data, dict)
        random_key = random.choice(list(record_data.keys()))
        print(record_data[random_key])
        print('Read array file as records.')


    def test_read_borealis_file_rawacf(self):
        print('Reading site file as records:')
        record_data = pydarn.read_borealis_file(borealis_site_rawacf_file, 'rawacf', site=True, records=True)
        self.assertIsInstance(record_data, dict)
        random_key = random.choice(list(record_data.keys()))
        print(record_data[random_key])
        print('Read site file as records.')

        print('Reading site file as arrays:')
        array_data = pydarn.read_borealis_file(borealis_site_rawacf_file, 'rawacf', site=True)
        self.assertIsInstance(array_data, dict)
        print(array_data['pulses'])
        print('Read site file as arrays.')

        print('Reading arrays file as arrays:')
        array_data = pydarn.read_borealis_file(borealis_array_rawacf_file, 'rawacf')
        self.assertIsInstance(array_data, dict)
        print(array_data['pulses'])
        print('Read arrays file as arrays.')

        print('Reading arrays file as records:')
        record_data = pydarn.read_borealis_file(borealis_array_rawacf_file, 'rawacf', records=True)
        self.assertIsInstance(record_data, dict)
        random_key = random.choice(list(record_data.keys()))
        print(record_data[random_key])
        print('Read array file as records.')


    def test_read_borealis_file_antennas_iq(self):
        print('Reading site file as records:')
        record_data = pydarn.read_borealis_file(borealis_site_antennas_iq_file, 'antennas_iq', site=True, records=True)
        self.assertIsInstance(record_data, dict)
        random_key = random.choice(list(record_data.keys()))
        print(record_data[random_key])
        print('Read site file as records.')

        print('Reading site file as arrays:')
        array_data = pydarn.read_borealis_file(borealis_site_antennas_iq_file, 'antennas_iq', site=True)
        self.assertIsInstance(array_data, dict)
        print(array_data['pulses'])
        print('Read site file as arrays.')

        print('Reading arrays file as arrays:')
        array_data = pydarn.read_borealis_file(borealis_array_antennas_iq_file, 'antennas_iq')
        self.assertIsInstance(array_data, dict)
        print(array_data['pulses'])
        print('Read arrays file as arrays.')

        print('Reading arrays file as records:')
        record_data = pydarn.read_borealis_file(borealis_array_antennas_iq_file, 'antennas_iq', records=True)
        self.assertIsInstance(record_data, dict)
        random_key = random.choice(list(record_data.keys()))
        print(record_data[random_key])
        print('Read array file as records.')


    def test_read_borealis_file_rawrf(self):
        # only site files and records exist for rawrf files.
        print('Reading site file as records:')
        record_data = pydarn.read_borealis_file(borealis_site_rawrf_file, 'rawrf', site=True, records=True)
        self.assertIsInstance(record_data, dict)
        random_key = random.choice(list(record_data.keys()))
        print(record_data[random_key])
        print('Read site file as records.')


    # add reader failure tests here
    # test reads with wrong filetype given (antennas_iq given bfiq flag especially)


    def test_write_borealis_file_rawacf(self):
        print('Writing a site file:')
        record_data = borealis_rawacf_data_sets.borealis_site_rawacf_data
        written_file = pydarn.write_borealis_file(record_data, 'test_write_borealis_file.rawacf.hdf5.site', 'rawacf', records=True)
        self.assertTrue(os.path.isfile(written_file))
        os.remove(written_file)
        print("Wrote a site file.")

        print('Writing an arrays file:')
        array_data = borealis_rawacf_data_sets.borealis_array_rawacf_data
        written_file = pydarn.write_borealis_file(array_data, 'test_write_borealis_file.rawacf.hdf5', 'rawacf')
        self.assertTrue(os.path.isfile(written_file))
        os.remove(written_file)
        print("Wrote an arrays file.")


    def test_write_borealis_file_bfiq(self):
        print('Writing a site file:')
        record_data = borealis_bfiq_data_sets.borealis_site_bfiq_data
        written_file = pydarn.write_borealis_file(record_data, 'test_write_borealis_file.bfiq.hdf5.site', 'bfiq', records=True)
        self.assertTrue(os.path.isfile(written_file))
        os.remove(written_file)
        print("Wrote a site file.")

        print('Writing an arrays file:')
        array_data = borealis_bfiq_data_sets.borealis_array_bfiq_data
        written_file = pydarn.write_borealis_file(array_data, 'test_write_borealis_file.bfiq.hdf5', 'bfiq')
        self.assertTrue(os.path.isfile(written_file))
        os.remove(written_file)
        print("Wrote an arrays file.")


    def test_write_borealis_file_antennas_iq(self):
        print('Writing a site file:')
        record_data = borealis_antennas_iq_data_sets.borealis_site_antennas_iq_data
        written_file = pydarn.write_borealis_file(record_data, 'test_write_borealis_file.antennas_iq.hdf5.site', 'antennas_iq', records=True)
        self.assertTrue(os.path.isfile(written_file))
        os.remove(written_file)
        print("Wrote a site file.")

        print('Writing an arrays file:')
        array_data = borealis_antennas_iq_data_sets.borealis_array_antennas_iq_data
        written_file = pydarn.write_borealis_file(array_data, 'test_write_borealis_file.antennas_iq.hdf5', 'antennas_iq')
        self.assertTrue(os.path.isfile(written_file))
        os.remove(written_file)
        print("Wrote an arrays file.")


    # add writer failure tests here


    def check_dictionaries_are_same(self, dict1, dict2):

        self.assertEqual(list(dict1.keys()), list(dict2.keys()))
        for key1, value1 in dict1.items():
            if isinstance(value1, dict) or isinstance(value1, OrderedDict):
                self.check_dictionaries_are_same(value1, dict2[key1])
            elif isinstance(value1, np.ndarray):
                self.assertTrue((value1 == dict2[key1]).all())
            else:
                self.assertEqual(value1, dict2[key1])

        return True


    def test_restructure_data_integrity_rawacf(self):
        test_rawacf_array_file = './test_rawacf_array_file.hdf5'
        test_rawacf_site_file = './test_rawacf_record_file.hdf5.site'
        pydarn.borealis_site_to_array_file(borealis_site_rawacf_file, test_rawacf_array_file)
        pydarn.borealis_array_to_site_file(test_rawacf_array_file, test_rawacf_site_file)
        original_dict = pydarn.read_borealis_file(borealis_site_rawacf_file, 'rawacf', site=True, records=True)
        processed_dict = pydarn.read_borealis_file(test_rawacf_site_file, 'rawacf', site=True, records=True)
        dictionaries_are_same = self.check_dictionaries_are_same(original_dict, processed_dict)
        self.assertTrue(dictionaries_are_same)
        print('Restructured site file is the same as original site file: {}'.format(dictionaries_are_same))
        os.remove(test_rawacf_array_file)
        os.remove(test_rawacf_site_file)


    def test_restructure_data_integrity_bfiq(self):
        test_bfiq_array_file = './test_bfiq_array_file.hdf5'
        test_bfiq_site_file = './test_bfiq_record_file.hdf5.site'
        pydarn.borealis_site_to_array_file(borealis_site_bfiq_file, test_bfiq_array_file)
        pydarn.borealis_array_to_site_file(test_bfiq_array_file, test_bfiq_site_file)
        original_dict = pydarn.read_borealis_file(borealis_site_bfiq_file, 'bfiq', site=True, records=True)
        processed_dict = pydarn.read_borealis_file(test_bfiq_site_file, 'bfiq', site=True, records=True)
        dictionaries_are_same = self.check_dictionaries_are_same(original_dict, processed_dict)
        self.assertTrue(dictionaries_are_same)
        print('Restructured site file is the same as original site file: {}'.format(dictionaries_are_same))
        os.remove(test_bfiq_array_file)
        os.remove(test_bfiq_site_file)


    def test_restructure_data_integrity_antennas_iq(self):
        test_antennas_iq_array_file = './test_antennas_iq_array_file.hdf5'
        test_antennas_iq_site_file = './test_antennas_iq_record_file.hdf5.site'
        pydarn.borealis_site_to_array_file(borealis_site_antennas_iq_file, test_antennas_iq_array_file)
        pydarn.borealis_array_to_site_file(test_antennas_iq_array_file, test_antennas_iq_site_file)
        original_dict = pydarn.read_borealis_file(borealis_site_antennas_iq_file, 'antennas_iq', site=True, records=True)
        processed_dict = pydarn.read_borealis_file(test_antennas_iq_site_file, 'antennas_iq', site=True, records=True)
        dictionaries_are_same = self.check_dictionaries_are_same(original_dict, processed_dict)
        self.assertTrue(dictionaries_are_same)
        print('Restructured site file is the same as original site file: {}'.format(dictionaries_are_same))
        os.remove(test_antennas_iq_array_file)
        os.remove(test_antennas_iq_site_file)


    # add array file read tests (after restructure)

    # add integrity tests of array -> site -> array



    def test_write_records_as_arrays(self):
        record_data = borealis_rawacf_data_sets.borealis_site_rawacf_data
        self.assertRaises(pydarn.borealis_exceptions.BorealisStructureError, pydarn.write_borealis_file,
            record_data, 'test_write_borealis_file.rawacf.hdf5', 'rawacf')
        print('Raises BorealisStructureError')


    def test_write_arrays_as_records(self):
        array_data = borealis_rawacf_data_sets.borealis_array_rawacf_data
        self.assertRaises(pydarn.borealis_exceptions.BorealisStructureError, pydarn.write_borealis_file,
            array_data, 'test_write_borealis_file.rawacf.hdf5', 'rawacf', records=True)
        print('Raises BorealisStructureError')


    def test_return_reader(self):
        record_data = pydarn.read_borealis_file(borealis_site_bfiq_file, 'bfiq', site=True, records=True)
        self.assertIsInstance(record_data, dict)
        random_key = random.choice(list(record_data.keys()))
        print(record_data[random_key])

        array_data = pydarn.return_reader(borealis_array_bfiq_file, 'bfiq', )
        self.assertIsInstance(array_data, dict)
        print(array_data['pulses'])

class TestBorealisSiteRead(unittest.TestCase):
    """
    Testing class for BorealisSiteRead
    """

    def setUp(self):
        rawacf_file_path = borealis_site_rawacf_file
        bfiq_file_path = borealis_site_bfiq_file
        antennas_file_path = borealis_site_antennas_iq_file
        rawrf_file_path = borealis_site_rawrf_file
        nonexistent_dir_path = './dog/somefile.rawacf'
        nonexistent_file_path = '../test_files/somefile.rawacf'
        empty_file_path = borealis_empty_file 

    def test_incorrect_path(self):
        """
        Testing BorealisSiteRead constructor with an nonexistent folder.

        Expected behaviour: raise OSError
        """
        self.assertRaises(OSError, pydarn.BorealisSiteRead,
                          nonexistent_dir_path, 'rawacf')

    def test_incorrect_file(self):
        """
        Tests if BorealisSiteRead constructor with an non-existent file

        Expected behaviour: raises OSError
        """
        self.assertRaises(OSError, pydarn.BorealisSiteRead,
                          nonexistent_file_path, 'rawacf')

    def test_empty_file(self):
        """
        Tests if BorealisSiteRead constructor with an empty file

        Expected behaviour: raise OSError, unable to open (file signature not found)
        """
        self.assertRaises(OSError,
                          pydarn.BorealisSiteRead, empty_file_path, 'rawacf')

    def test_read_bfiq(self):
        """
        Test reading records from bfiq.

        Checks:
            - returns correct data structures
            - returns expected values
        """
        dm = pydarn.BorealisSiteRead(bfiq_file_path, 'bfiq')
        records = dm.records
        first_record = records[dm.group_names[0]]
        self.assertIsInstance(records, collections.OrderedDict)
        self.assertIsInstance(first_record, dict)
        self.assertIsInstance(first_record['num_slices'], np.int64)

    def test_read_rawacf(self):
        """
        Test reading records from rawacf.

        Checks:
            - returns correct data structures
            - returns expected values
        """
        dm = pydarn.BorealisSiteRead(rawacf_file_path, 'rawacf')
        records = dm.records
        first_record = records[dm.group_names[0]]
        self.assertIsInstance(records, collections.OrderedDict)
        self.assertIsInstance(first_record, dict)
        self.assertIsInstance(first_record['num_slices'], np.int64)

    def test_read_antennas_iq(self):
        """
        Test reading records from antennas_iq.

        Checks:
            - returns correct data structures
            - returns expected values
        """
        dm = pydarn.BorealisSiteRead(antennas_file_path, 'antennas_iq')
        records = dm.records
        first_record = records[dm.group_names[0]]
        self.assertIsInstance(records, collections.OrderedDict)
        self.assertIsInstance(first_record, dict)
        self.assertIsInstance(first_record['num_slices'], np.int64)

    def test_read_rawrf(self):
        """
        Test reading records from antennas_iq.

        Checks:
            - returns correct data structures
            - returns expected values
        """
        dm = pydarn.BorealisSiteRead(rawrf_file_path, 'rawrf')
        records = dm.records
        first_record = records[dm.group_names[0]]
        self.assertIsInstance(records, collections.OrderedDict)
        self.assertIsInstance(first_record, dict)
        self.assertIsInstance(first_record['num_slices'], np.int64)


class TestBorealisSiteWrite(unittest.TestCase):
    """
    Tests BorealisSiteWrite class
    """

    def setUp(self):
        rawacf_site_data = copy.deepcopy(
            borealis_rawacf_data_sets.borealis_site_rawacf_data)
        rawacf_site_missing_field = copy.deepcopy(
            borealis_rawacf_data_sets.borealis_site_rawacf_data)
        rawacf_site_extra_field = copy.deepcopy(
            borealis_rawacf_data_sets.borealis_site_rawacf_data)
        rawacf_site_incorrect_fmt = copy.deepcopy(
            borealis_rawacf_data_sets.borealis_site_rawacf_data)
        bfiq_site_data = copy.deepcopy(
            borealis_bfiq_site_data_sets.borealis_site_bfiq_site_data)
        bfiq_site_missing_field = copy.deepcopy(
            borealis_bfiq_site_data_sets.borealis_site_bfiq_site_data)
        bfiq_site_extra_field = copy.deepcopy(
            borealis_bfiq_site_data_sets.borealis_site_bfiq_site_data)
        bfiq_site_incorrect_fmt = copy.deepcopy(
            borealis_bfiq_site_data_sets.borealis_site_bfiq_site_data)

    def test_writing_rawacf(self):
        """
        Tests write_rawacf method - writes a rawacf file

        Expected behaviour
        ------------------
        Rawacf file is produced
        """

        writer = pydarn.BorealisSiteWrite("test_rawacf.rawacf.hdf5", 
                                          rawacf_site_data, 'rawacf')
        # only testing the file is created since it should only be created
        # at the last step after all checks have passed
        # Testing the integrity of the insides of the file will be part of
        # integration testing since we need BorealisSiteRead for that.
        self.assertTrue(os.path.isfile("test_rawacf.rawacf.hdf5"))
        os.remove("test_rawacf.rawacf.hdf5")

    def test_missing_field_rawacf(self):
        """
        Tests write_rawacf method - writes a rawacf structure file for the
        given data

        Expected behaviour
        ------------------
        Raises BorealisFieldMissingError - because the rawacf data is
        missing field num_sequences
        """

        keys = sorted(list(rawacf_site_missing_field.keys()))
        del rawacf_site_missing_field[keys[0]]['num_sequences']

        try:
            writer = pydarn.BorealisSiteWrite(
                "test_rawacf.rawacf.hdf5", rawacf_site_missing_field, 'rawacf')
        except pydarn.borealis_exceptions.BorealisFieldMissingError as err:
            self.assertEqual(err.fields, {'num_sequences'})
            self.assertEqual(err.record_name, keys[0])

    def test_extra_field_rawacf(self):
        """
        Tests write_rawacf method - writes a rawacf structure file for the
        given data

        Expected behaviour
        ------------------
        Raises BorealisExtraFieldError because the rawacf data
        has an extra field dummy
        """
        keys = sorted(list(rawacf_site_extra_field.keys()))
        rawacf_site_extra_field[keys[0]]['dummy'] = 'dummy'
        try:
            writer = pydarn.BorealisSiteWrite(
                "test_rawacf.rawacf.hdf5", rawacf_site_extra_field, 'rawacf')
        except pydarn.borealis_exceptions.BorealisExtraFieldError as err:
            self.assertEqual(err.fields, {'dummy'})
            self.assertEqual(err.record_name, keys[0])

    def test_incorrect_data_format_rawacf(self):
        """
        Tests write_rawacf method - writes a rawacf structure file for the
        given data

        Expected Behaviour
        -------------------
        Raises BorealisDataFormatTypeError because the rawacf data has the
        wrong type for the scan_start_marker field
        """
        keys = sorted(list(rawacf_site_incorrect_fmt.keys()))
        rawacf_site_incorrect_fmt[keys[0]]['scan_start_marker'] = 1


        try:
            writer = pydarn.BorealisSiteWrite(
                "test_rawacf.rawacf.hdf5", rawacf_site_incorrect_fmt, 'rawacf')
        except pydarn.borealis_exceptions.BorealisDataFormatTypeError as err:
            self.assertEqual(
                err.incorrect_params['scan_start_marker'], "<class 'numpy.bool_'>")
            self.assertEqual(err.record_name, keys[0])

    def test_writing_bfiq(self):
        """
        Tests write_bfiq method - writes a bfiq file

        Expected behaviour
        ------------------
        bfiq file is produced
        """
        writer = pydarn.BorealisSiteWrite("test_bfiq.bfiq.hdf5", bfiq_site_data, 'bfiq')
        # only testing the file is created since it should only be created
        # at the last step after all checks have passed
        # Testing the integrity of the insides of the file will be part of
        # integration testing since we need BorealisSiteRead for that.
        self.assertTrue(os.path.isfile("test_bfiq.bfiq.hdf5"))
        os.remove("test_bfiq.bfiq.hdf5")

    def test_missing_field_bfiq(self):
        """
        Tests write_bfiq method - writes a bfiq structure file for the
        given data

        Expected behaviour
        ------------------
        Raises BorealisFieldMissingError - because the bfiq data is
        missing field antenna_arrays_order
        """
        keys = sorted(list(bfiq_site_missing_field.keys()))
        del bfiq_site_missing_field[keys[0]]['antenna_arrays_order']
        
        try:
            writer = pydarn.BorealisSiteWrite(
                "test_bfiq.bfiq.hdf5", bfiq_site_missing_field, 'bfiq')
        except pydarn.borealis_exceptions.BorealisFieldMissingError as err:
            self.assertEqual(err.fields, {'antenna_arrays_order'})
            self.assertEqual(err.record_name, keys[0])

    def test_extra_field_bfiq(self):
        """
        Tests write_bfiq method - writes a bfiq structure file for the
        given data

        Expected behaviour
        ------------------
        Raises BorealisExtraFieldError because the bfiq data
        has an extra field dummy
        """
        keys = sorted(list(bfiq_site_extra_field.keys()))
        bfiq_site_extra_field[keys[0]]['dummy'] = 'dummy'

        try:
            writer = pydarn.BorealisSiteWrite("test_bfiq.bfiq.hdf5", 
                bfiq_site_extra_field, 'bfiq')
        except pydarn.borealis_exceptions.BorealisExtraFieldError as err:
            self.assertEqual(err.fields, {'dummy'})
            self.assertEqual(err.record_name, keys[0])

    def test_incorrect_data_format_bfiq(self):
        """
        Tests write_bfiq method - writes a bfiq structure file for the
        given data

        Expected Behaviour
        -------------------
        Raises BorealisDataFormatTypeError because the bfiq data has the
        wrong type for the first_range_rtt field
        """
        keys = sorted(list(bfiq_site_incorrect_fmt.keys()))
        bfiq_site_incorrect_fmt[keys[0]]['first_range_rtt'] = 5


        try:
            writer = pydarn.BorealisSiteWrite(
                "test_bfiq.bfiq.hdf5", bfiq_site_incorrect_fmt, 'bfiq')
        except pydarn.borealis_exceptions.BorealisDataFormatTypeError as err:
            self.assertEqual(
                err.incorrect_params['first_range_rtt'], "<class 'numpy.float32'>")
            self.assertEqual(err.record_name, keys[0])


class TestBorealisArrayRead(unittest.TestCase):
    """
    Testing class for BorealisArrayRead
    """

    def setUp(self):
        rawacf_file_path = borealis_array_rawacf_file
        bfiq_file_path = borealis_array_bfiq_file
        antennas_file_path = borealis_array_antennas_iq_file
        nonexistent_dir_path = './dog/somefile.rawacf'
        nonexistent_file_path = '../test_files/somefile.rawacf'
        empty_file_path = borealis_empty_file 

    def test_incorrect_path(self):
        """
        Testing BorealisArrayRead constructor with an nonexistent folder.

        Expected behaviour: raise OSError
        """
        self.assertRaises(OSError, pydarn.BorealisArrayRead,
                          nonexistent_dir_path, 'rawacf')

    def test_incorrect_file(self):
        """
        Tests if BorealisArrayRead constructor with an non-existent file

        Expected behaviour: raises OSError
        """
        self.assertRaises(OSError, pydarn.BorealisArrayRead,
                          nonexistent_file_path, 'rawacf')

    def test_empty_file(self):
        """
        Tests if BorealisArrayRead constructor with an empty file

        Expected behaviour: raise OSError, unable to open (file signature not found)
        """
        self.assertRaises(OSError,
                          pydarn.BorealisArrayRead, empty_file_path, 'rawacf')

    def test_read_bfiq(self):
        """
        Test reading records from bfiq.

        Checks:
            - returns correct data structures
            - returns expected values
        """
        dm = pydarn.BorealisArrayRead(bfiq_file_path, 'bfiq')
        records = dm.records
        first_record = records[dm.group_names[0]]
        self.assertIsInstance(records, collections.OrderedDict)
        self.assertIsInstance(first_record, dict)
        self.assertIsInstance(first_record['num_slices'], np.int64)

    def test_read_rawacf(self):
        """
        Test reading records from rawacf.

        Checks:
            - returns correct data structures
            - returns expected values
        """
        dm = pydarn.BorealisArrayRead(rawacf_file_path, 'rawacf')
        records = dm.records
        first_record = records[dm.group_names[0]]
        self.assertIsInstance(records, collections.OrderedDict)
        self.assertIsInstance(first_record, dict)
        self.assertIsInstance(first_record['num_slices'], np.int64)

    def test_read_antennas_iq(self):
        """
        Test reading records from bfiq.

        Checks:
            - returns correct data structures
            - returns expected values
        """
        dm = pydarn.BorealisArrayRead(antennas_file_path, 'antennas_iq')
        records = dm.records
        first_record = records[dm.group_names[0]]
        self.assertIsInstance(records, collections.OrderedDict)
        self.assertIsInstance(first_record, dict)
        self.assertIsInstance(first_record['num_slices'], np.int64)   


class TestBorealisArrayWrite(unittest.TestCase):
    """
    Tests BorealisArrayWrite class
    """

    def setUp(self):
        rawacf_array_data = copy.deepcopy(
            borealis_rawacf_data_sets.borealis_array_rawacf_data)
        rawacf_array_missing_field = copy.deepcopy(
            borealis_rawacf_data_sets.borealis_array_rawacf_data)
        rawacf_array_extra_field = copy.deepcopy(
            borealis_rawacf_data_sets.borealis_array_rawacf_data)
        rawacf_array_incorrect_fmt = copy.deepcopy(
            borealis_rawacf_data_sets.borealis_array_rawacf_data)
        bfiq_array_data = copy.deepcopy(
            borealis_bfiq_array_data_sets.borealis_array_bfiq_array_data)
        bfiq_array_missing_field = copy.deepcopy(
            borealis_bfiq_array_data_sets.borealis_array_bfiq_array_data)
        bfiq_array_extra_field = copy.deepcopy(
            borealis_bfiq_array_data_sets.borealis_array_bfiq_array_data)
        bfiq_array_incorrect_fmt = copy.deepcopy(
            borealis_bfiq_array_data_sets.borealis_array_bfiq_array_data)

    def test_writing_rawacf(self):
        """
        Tests write_rawacf method - writes a rawacf file

        Expected behaviour
        ------------------
        Rawacf file is produced
        """

        writer = pydarn.BorealisArrayWrite("test_rawacf.rawacf.hdf5", 
                                          rawacf_array_data, 'rawacf')
        # only testing the file is created since it should only be created
        # at the last step after all checks have passed
        self.assertTrue(os.path.isfile("test_rawacf.rawacf.hdf5"))
        os.remove("test_rawacf.rawacf.hdf5")

    def test_missing_field_rawacf(self):
        """
        Tests write_rawacf method - writes a rawacf structure file for the
        given data

        Expected behaviour
        ------------------
        Raises BorealisFieldMissingError - because the rawacf data is
        missing field num_sequences
        """

        keys = sorted(list(rawacf_array_missing_field.keys()))
        del rawacf_array_missing_field[keys[0]]['num_sequences']

        try:
            writer = pydarn.BorealisArrayWrite(
                "test_rawacf.rawacf.hdf5", rawacf_array_missing_field, 'rawacf')
        except pydarn.borealis_exceptions.BorealisFieldMissingError as err:
            self.assertEqual(err.fields, {'num_sequences'})
            self.assertEqual(err.record_name, keys[0])

    def test_extra_field_rawacf(self):
        """
        Tests write_rawacf method - writes a rawacf structure file for the
        given data

        Expected behaviour
        ------------------
        Raises BorealisExtraFieldError because the rawacf data
        has an extra field dummy
        """
        keys = sorted(list(rawacf_array_extra_field.keys()))
        rawacf_array_extra_field[keys[0]]['dummy'] = 'dummy'
        try:
            writer = pydarn.BorealisArrayWrite(
                "test_rawacf.rawacf.hdf5", rawacf_array_extra_field, 'rawacf')
        except pydarn.borealis_exceptions.BorealisExtraFieldError as err:
            self.assertEqual(err.fields, {'dummy'})
            self.assertEqual(err.record_name, keys[0])

    def test_incorrect_data_format_rawacf(self):
        """
        Tests write_rawacf method - writes a rawacf structure file for the
        given data

        Expected Behaviour
        -------------------
        Raises BorealisDataFormatTypeError because the rawacf data has the
        wrong type for the scan_start_marker field
        """
        keys = sorted(list(rawacf_array_incorrect_fmt.keys()))
        rawacf_array_incorrect_fmt[keys[0]]['scan_start_marker'] = 1


        try:
            writer = pydarn.BorealisArrayWrite(
                "test_rawacf.rawacf.hdf5", rawacf_array_incorrect_fmt, 'rawacf')
        except pydarn.borealis_exceptions.BorealisDataFormatTypeError as err:
            self.assertEqual(
                err.incorrect_params['scan_start_marker'], "<class 'numpy.bool_'>")
            self.assertEqual(err.record_name, keys[0])

    def test_writing_bfiq(self):
        """
        Tests write_bfiq method - writes a bfiq file

        Expected behaviour
        ------------------
        bfiq file is produced
        """
        writer = pydarn.BorealisArrayWrite("test_bfiq.bfiq.hdf5", bfiq_array_data, 'bfiq')
        # only testing the file is created since it should only be created
        # at the last step after all checks have passed
        # Testing the integrity of the insides of the file will be part of
        # integration testing since we need BorealisArrayRead for that.
        self.assertTrue(os.path.isfile("test_bfiq.bfiq.hdf5"))
        os.remove("test_bfiq.bfiq.hdf5")

    def test_missing_field_bfiq(self):
        """
        Tests write_bfiq method - writes a bfiq structure file for the
        given data

        Expected behaviour
        ------------------
        Raises BorealisFieldMissingError - because the bfiq data is
        missing field antenna_arrays_order
        """
        keys = sorted(list(bfiq_array_missing_field.keys()))
        del bfiq_array_missing_field[keys[0]]['antenna_arrays_order']
        
        try:
            writer = pydarn.BorealisArrayWrite(
                "test_bfiq.bfiq.hdf5", bfiq_array_missing_field, 'bfiq')
        except pydarn.borealis_exceptions.BorealisFieldMissingError as err:
            self.assertEqual(err.fields, {'antenna_arrays_order'})
            self.assertEqual(err.record_name, keys[0])

    def test_extra_field_bfiq(self):
        """
        Tests write_bfiq method - writes a bfiq structure file for the
        given data

        Expected behaviour
        ------------------
        Raises BorealisExtraFieldError because the bfiq data
        has an extra field dummy
        """
        keys = sorted(list(bfiq_array_extra_field.keys()))
        bfiq_array_extra_field[keys[0]]['dummy'] = 'dummy'

        try:
            writer = pydarn.BorealisArrayWrite("test_bfiq.bfiq.hdf5", 
                bfiq_array_extra_field, 'bfiq')
        except pydarn.borealis_exceptions.BorealisExtraFieldError as err:
            self.assertEqual(err.fields, {'dummy'})
            self.assertEqual(err.record_name, keys[0])

    def test_incorrect_data_format_bfiq(self):
        """
        Tests write_bfiq method - writes a bfiq structure file for the
        given data

        Expected Behaviour
        -------------------
        Raises BorealisDataFormatTypeError because the bfiq data has the
        wrong type for the first_range_rtt field
        """
        keys = sorted(list(bfiq_array_incorrect_fmt.keys()))
        bfiq_array_incorrect_fmt[keys[0]]['first_range_rtt'] = 5


        try:
            writer = pydarn.BorealisArrayWrite(
                "test_bfiq.bfiq.hdf5", bfiq_array_incorrect_fmt, 'bfiq')
        except pydarn.borealis_exceptions.BorealisDataFormatTypeError as err:
            self.assertEqual(
                err.incorrect_params['first_range_rtt'], "<class 'numpy.float32'>")
            self.assertEqual(err.record_name, keys[0])


class TestBorealisConvert(unittest.TestCase):
    """
    Tests BorealisConvert class
    """

    def setUp(self):
        rawacf_file_path = borealis_site_rawacf_file
        bfiq_file_path = borealis_site_bfiq_file

    def test_borealis_convert_constructor(self):
        """
        Tests BorealisConvert constructor

        Expected behaviour
        ------------------
        Contains file name of the data if given to it.
        """
        converter = pydarn.BorealisConvert(rawacf_file_path)
        self.assertIsInstance(converter.group_names, list)
        self.assertGreater(len(converter.group_names), 0)
        self.assertEqual(converter.origin_filetype, 'rawacf')

    def test_borealis_convert_to_rawacf(self):
        """
        Tests BorealisConvert to rawacf

        Expected behaviour
        ------------------
        write a darn rawacf
        """
        converter = pydarn.BorealisConvert(rawacf_file_path)
        converter.write_to_dmap("rawacf", "test_rawacf.rawacf.dmap")

        # only testing the file is created since it should only be created
        # at the last step after all checks have passed
        # Testing the integrity of the insides of the file will be part of
        # integration testing since we need BorealisSiteRead for that.
        self.assertTrue(os.path.isfile("test_rawacf.rawacf.dmap"))
        os.remove("test_rawacf.rawacf.dmap")

    def test_borealis_convert_to_iqdat(self):
        """
        Tests BorealisConvert to iqdat

        Expected behaviour
        ------------------
        write a darn iqdat
        """
        converter = pydarn.BorealisConvert(bfiq_file_path)
        converter.write_to_dmap("iqdat", "test_iqdat.iqdat.dmap")

        # only testing the file is created since it should only be created
        # at the last step after all checks have passed
        # Testing the integrity of the insides of the file will be part of
        # integration testing since we need BorealisSiteRead for that.
        self.assertTrue(os.path.isfile("test_iqdat.iqdat.dmap"))
        os.remove("test_iqdat.iqdat.dmap")
