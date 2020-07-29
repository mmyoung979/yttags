// React imports
import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';

// Redux imports
import { Provider } from 'react-redux';
import store from '../store';

// Project imports
import Tags from './Tags';

// App
class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Fragment>
          <Tags />
        </Fragment>
      </Provider>
    )
  }
}

// Export app
ReactDOM.render(<App />, document.getElementById('app'));
