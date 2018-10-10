import React, { Component } from 'react';

class Layer extends Component {

    componentDidMount() {

    }

    render() {
        return (
            <div className="Layer">
                <div className="content has-text-left">
                    <h2 className="subtitle is-size-5">Camadas</h2>
                    <div>
                        <input type="checkbox" name="ndvi" onClick={() => this.props.onChange('ndvi')} /><span> NDVI</span>
                    </div>
                    <div>
                        <input type="checkbox" name="truecolor" onClick={() => this.props.onChange('trueColor')} /><span> True Color</span>
                    </div>
                </div>
            </div>
    );
  }
}

export default Layer;
