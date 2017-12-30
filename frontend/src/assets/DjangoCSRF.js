import React, {
    PropTypes,
} from 'react';

import {csrftoken} from './csrf'; 

const DjangoCSRF = () => {
    return (
        <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
    );
};


export default DjangoCSRF;