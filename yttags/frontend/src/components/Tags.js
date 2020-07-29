import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getTags } from '../actions/tags';

export class Tags extends Component {
  static propTypes = {
    tags: PropTypes.array.isRequired
  };

  componentDidMount() {
    this.props.getTags();
  }

  render() {
    return (
      <Fragment>
        <table className="table table-bordered">
          <thead className="thead-dark">
            <tr>
              <th className="text-center" scope="col">Video IDs</th>
            </tr>
          </thead>
          <tbody>
            { this.props.tags.map(tag => (
              <tr key={tag.youtube_id}>
                <td className="col-lg-3 col-md-4 col-sm-6 col-xs-12 text-center">
                  <a href={"https://www.youtube.com/watch?v=" + tag.youtube_id} target="_blank">
                    <p className="tag">{tag.youtube_id}</p>
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    )
  }
}

const mapStateToProps = state => ({
  tags: state.tags.tags
})

export default connect(mapStateToProps, { getTags })(Tags);
