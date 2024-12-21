var dagfuncs = (window.dashAgGridFunctions = window.dashAgGridFunctions || {});

const {useRef, createElement, useEffect, useCallback, forwardRef, useMemo} = React

// Use this with DMC components
dagfuncs.AllFunctionalComponentEditors = forwardRef(({ value, ...params }, ref) => {
    const comp = params.colDef.cellEditorParams.component;
    const node = useRef(params.api.getRowNode(params.node.id));
    const newValue = useRef(value);
    const escaped = useRef(null);
    const editorRef = useRef(null);

    const handleStop = ({ event, ...params }) => {
        setTimeout(() => {
            if (!escaped.current) {
                node.current.setDataValue(params.column.colId, newValue.current);
            }
        }, 1);
    };

    if (params.colDef.cellEditorPopup) {
        comp['props']['style'] = { ...comp.props?.style, width: params.column.actualWidth - 2 };
    }

    const setProps = (propsToSet) => {
        if ('value' in propsToSet) {
            newValue.current = propsToSet.value;
        }
    };

    const handleKeyDown = ({ key, ...event }) => {
        if (key == "Escape") {
            escaped.current = true;
        }
    };

    useEffect(() => {
        params.api.addEventListener('cellEditingStopped', handleStop);
        document.addEventListener('keydown', handleKeyDown);
        params.colDef.suppressKeyboardEvent = (params) => params.editing && params.event.key != 'Tab';
        return () => {
            document.removeEventListener('keydown', handleKeyDown);
            delete params.colDef.suppressKeyboardEvent;
            params.api.removeEventListener('cellEditingStopped', handleStop);
        };
    }, []);

    useEffect(() => {
        if (editorRef.current) {
            if (editorRef.current.querySelector('input')) {
                editorRef.current.querySelector('input').focus();
            } else {
                editorRef.current.focus()
            }
        }
    }, [editorRef.current]);

    const el = useMemo(() =>
        createElement(
            'div',
            { ref: editorRef, tabIndex: 0 },
            createElement(window[comp['namespace']][comp['type']], { ...comp.props, setProps, value })
        ),
    []);

    return el;
});

// Use this with most dash-core-components
dagfuncs.AllComponentEditors = class {
    // gets called once before the renderer is used
    init(params) {

        // create the cell
        this.params = params;

        this.eInput = document.createElement('div');

        this.root = ReactDOM.createRoot(this.eInput)

        // sets editor value to the value from the cell
        this.value = params.value;
    }

    // gets called once when grid ready to insert the element
    getGui() {
        return this.eInput;
    }

    // focus and select can be done after the gui is attached
    afterGuiAttached() {
        const comp = this.params.colDef.cellEditorParams.component
        this.params.colDef.suppressKeyboardEvent = (params) => params.editing && params.event.key != 'Tab'
        if (this.params.colDef.cellEditorPopup) {
            comp['props']['style'] = {...comp.props?.style, width: this.params.column.actualWidth-2}
        }

        const setProps = (propsToSet) => {
            if ('value' in propsToSet) {
               this.value = propsToSet.value
            }
            this.root.render(
                createElement(window[comp.namespace][comp.type], {...comp.props, value: this.value, setProps})
            )
        }

        this.root.render(
            createElement(window[comp.namespace][comp.type], {...comp.props, value: this.value, setProps})
        )

    }

    // returns the new value after editing
    getValue() {
        delete this.params.colDef.suppressKeyboardEvent
        return this.value;
    }
};