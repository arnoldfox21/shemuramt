import React from 'react';
import Axios from 'axios';

export default {

	send_data: function(to, pk, j){
		Axios({
			  method: 'post',
			  url: to,
			  data: {
			    id: pk,
			    jumlah: j
			  }
			});

		}
	}