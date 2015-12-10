#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mock import patch
import httpretty
from httpretty.core import HTTPrettyRequest, HTTPrettyRequestEmpty


@patch('httpretty.httpretty')
def test_last_request(original):
    """httpretty.last_request() should return httpretty.core.last_request"""

    httpretty.last_request().should.equal(original.last_request)

def test_has_request():
    """httpretty.has_request() correctly detects whether or not a request has been made"""
    httpretty.has_request().should.be.false
    with patch('httpretty.httpretty.last_request', return_value=HTTPrettyRequest('')):
        httpretty.has_request().should.be.true

def test_all_requests():
    """httpretty.all_request() correctly returns all requests made"""
    httpretty.all_requests().should.equal([])

    httpretty.httpretty.latest_requests = [HTTPrettyRequestEmpty(), HTTPrettyRequestEmpty()]
    httpretty.all_requests().should.equal(httpretty.httpretty.latest_requests)
    httpretty.httpretty.latest_requests = []

def test_request_count():
    """httpretty correctly returns number of requests made"""
    httpretty.request_count().should.equal(0)

    with patch('httpretty.all_requests', return_value=[HTTPrettyRequestEmpty(), HTTPrettyRequestEmpty()]):
        httpretty.request_count().should.equal(2)
