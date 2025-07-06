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
