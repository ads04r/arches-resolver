import $ from 'jquery';
import ko from 'knockout';
import arches from 'arches';

import ResolverTemplate from 'templates/views/components/plugins/resolver.htm';

export default ko.components.register('resolver', {

		viewModel: function(params) {

		    var self = this; console.log(self);

		},
		template: ResolverTemplate

});
