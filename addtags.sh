#!/bin/bash

# Function to wrap verses, choruses, and other special cases with specific tags
wrap_sections() {
    local input_file="$1"
    local inside_block=0
    local in_chordpro=0
    local block_name
    local previous_line_empty=1

    while IFS= read -r line; do
        # Detect the start or end of a chordpro block
        if [[ "$line" == '```chordpro' ]]; then
            in_chordpro=1
            printf "%s\n" "$line"
            continue
        elif [[ "$line" == '```' ]]; then
            in_chordpro=0
            printf "%s\n" "$line"
            continue
        fi

        # Check if inside a chordpro block and process comment lines
        if [[ $in_chordpro -eq 1 ]]; then
            if [[ $previous_line_empty -eq 1 && "$line" =~ ^[[:alnum:]][^][]*$ ]]; then
                # Convert line to {c: ...} if it is the first line after a newline and does not contain brackets
                printf "{c: %s}\n" "$line"
            else
                printf "%s\n" "$line"
            fi
            previous_line_empty=0
            [[ -z "$line" ]] && previous_line_empty=1
            continue
        fi

        # Check for the beginning of a new block, case-insensitive
        if [[ "$line" =~ ^([Vv][Ee][Rr][Ss][Ee]|[Cc][Hh][Oo][Rr][Uu][Ss])([[:space:]]*[0-9]*)?$ ]]; then
            block_name=$(echo "$line" | awk '{print toupper($1)}')
            block_number=$(echo "$line" | awk '{print $2}')

            if [[ -n "$block_number" ]]; then
                block_name="${block_name} ${block_number}"
            fi

            if [[ "$block_name" =~ ^VERSE ]]; then
                printf "{sov: %s}\n" "$block_name"
                inside_block=1
            elif [[ "$block_name" =~ ^CHORUS ]]; then
                printf "{soc: %s}\n" "$block_name"
                inside_block=2
            fi
        # Check for the end of a block
        elif [[ -z "$line" && $inside_block -ne 0 ]]; then
            if [[ $inside_block -eq 1 ]]; then
                printf "{eov}\n\n"
            elif [[ $inside_block -eq 2 ]]; then
                printf "{eoc}\n\n"
            fi
            inside_block=0
        else
            # Continue writing the block's content
            printf "%s\n" "$line"
        fi
    done < "$input_file"

    # Ensure the last block is closed if file doesn't end with a newline
    if [[ $inside_block -eq 1 ]]; then
        printf "{eov}\n"
    elif [[ $inside_block -eq 2 ]]; then
        printf "{eoc}\n"
    fi
}

main() {
    local input_file="$1"

    if [[ -z "$input_file" ]]; then
        printf "Error: No input file provided.\n" >&2
        return 1
    elif [[ ! -f "$input_file" ]]; then
        printf "Error: The file '%s' does not exist.\n" "$input_file" >&2
        return 1
    fi

    wrap_sections "$input_file"
}

main "$1"
