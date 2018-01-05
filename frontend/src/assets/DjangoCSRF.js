import React, {
    PropTypes,
} from 'react';

import {csrftoken} from './csrf'; 

const DjangoCSRF = () => {
    return (
        <input type="hidden" name="csrfmiddlewaretoken" value='8tK25IgH8RI1G3kKvlQPGctgV7HglWxgakEDjXscqmZKApqGwLD7BGYNqVz3wzpV' />
    );
};


export default DjangoCSRF;