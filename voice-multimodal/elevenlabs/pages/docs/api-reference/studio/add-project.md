---
title: "Create Studio Project"
source: https://elevenlabs.io/docs/api-reference/studio/add-project.md
path: docs/api-reference/studio/add-project
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Studio Project

POST https://api.elevenlabs.io/v1/studio/projects
Content-Type: multipart/form-data

Creates a new Studio project, it can be either initialized as blank, from a document or from a URL.

Reference: https://elevenlabs.io/docs/api-reference/studio/add-project

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/studio/projects:
    post:
      operationId: create
      summary: Create Studio Project
      description: >-
        Creates a new Studio project, it can be either initialized as blank,
        from a document or from a URL.
      tags:
        - projects
      parameters:
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AddProjectResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: >-
                    The name of the Studio project, used for identification
                    only.
                default_title_voice_id:
                  type:
                    - string
                    - 'null'
                  description: >-
                    The voice_id that corresponds to the default voice used for
                    new titles.
                default_paragraph_voice_id:
                  type:
                    - string
                    - 'null'
                  description: >-
                    The voice_id that corresponds to the default voice used for
                    new paragraphs.
                default_model_id:
                  type:
                    - string
                    - 'null'
                  description: >-
                    The ID of the model to be used for this Studio project, you
                    can query GET /v1/models to list all available models.
                from_url:
                  type:
                    - string
                    - 'null'
                  description: >-
                    An optional URL from which we will extract content to
                    initialize the Studio project. If this is set, 'from_url'
                    and 'from_content' must be null. If neither 'from_url',
                    'from_document', 'from_content' are provided we will
                    initialize the Studio project as blank.
                from_document:
                  type: string
                  format: binary
                  description: >-
                    An optional .epub, .pdf, .txt or similar file can be
                    provided. If provided, we will initialize the Studio project
                    with its content. If this is set, 'from_url' and
                    'from_content' must be null. If neither 'from_url',
                    'from_document', 'from_content' are provided we will
                    initialize the Studio project as blank.
                from_content_json:
                  type: string
                  description: |2-

                        An optional content to initialize the Studio project with. If this is set, 'from_url' and 'from_document' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

                        Example:
                        [{"name": "Chapter A", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "A", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "B", "type": "tts_node"}]}, {"sub_type": "h1", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "C", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "D", "type": "tts_node"}]}]}, {"name": "Chapter B", "blocks": [{"sub_type": "p", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "E", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "F", "type": "tts_node"}]}, {"sub_type": "h2", "nodes": [{"voice_id": "6lCwbsX1yVjD49QmpkT0", "text": "G", "type": "tts_node"}, {"voice_id": "6lCwbsX1yVjD49QmpkT1", "text": "H", "type": "tts_node"}]}]}]
                        
                quality_preset:
                  $ref: '#/components/schemas/QualityPresetType'
                  default: standard
                  description: >
                    Output quality of the generated audio. Must be one of:

                    'standard' - standard output format, 128kbps with 44.1kHz
                    sample rate.

                    'high' - high quality output format, 192kbps with 44.1kHz
                    sample rate and major improvements on our side.

                    'ultra' - ultra quality output format, 192kbps with 44.1kHz
                    sample rate and highest improvements on our side.

                    'ultra_lossless' - ultra quality output format, 705.6kbps
                    with 44.1kHz sample rate and highest improvements on our
                    side in a fully lossless format.
                title:
                  type:
                    - string
                    - 'null'
                  description: >-
                    An optional name of the author of the Studio project, this
                    will be added as metadata to the mp3 file on Studio project
                    or chapter download.
                author:
                  type:
                    - string
                    - 'null'
                  description: >-
                    An optional name of the author of the Studio project, this
                    will be added as metadata to the mp3 file on Studio project
                    or chapter download.
                description:
                  type:
                    - string
                    - 'null'
                  description: An optional description of the Studio project.
                genres:
                  type: array
                  items:
                    type: string
                  description: >-
                    An optional list of genres associated with the Studio
                    project.
                target_audience:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaTargetAudience
                    - type: 'null'
                  description: An optional target audience of the Studio project.
                language:
                  type:
                    - string
                    - 'null'
                  description: >-
                    An optional language of the Studio project. Two-letter
                    language code (ISO 639-1).
                content_type:
                  type:
                    - string
                    - 'null'
                  description: An optional content type of the Studio project.
                original_publication_date:
                  type:
                    - string
                    - 'null'
                  description: >-
                    An optional original publication date of the Studio project,
                    in the format YYYY-MM-DD or YYYY.
                mature_content:
                  type:
                    - boolean
                    - 'null'
                  default: false
                  description: >-
                    An optional specification of whether this Studio project
                    contains mature content.
                isbn_number:
                  type:
                    - string
                    - 'null'
                  description: >-
                    An optional ISBN number of the Studio project you want to
                    create, this will be added as metadata to the mp3 file on
                    Studio project or chapter download.
                acx_volume_normalization:
                  type: boolean
                  default: false
                  description: >-
                    [Deprecated] When the Studio project is downloaded, should
                    the returned audio have postprocessing in order to make it
                    compliant with audiobook normalized volume requirements
                volume_normalization:
                  type: boolean
                  default: false
                  description: >-
                    When the Studio project is downloaded, should the returned
                    audio have postprocessing in order to make it compliant with
                    audiobook normalized volume requirements
                pronunciation_dictionary_locators:
                  type: array
                  items:
                    type: string
                  description: >-
                    A list of pronunciation dictionary locators
                    (pronunciation_dictionary_id, version_id) encoded as a list
                    of JSON strings for pronunciation dictionaries to be applied
                    to the text. A list of json encoded strings is required as
                    adding projects may occur through formData as opposed to
                    jsonBody. To specify multiple dictionaries use multiple
                    --form lines in your curl, such as --form
                    'pronunciation_dictionary_locators="{\"pronunciation_dictionary_id\":\"Vmd4Zor6fplcA7WrINey\",\"version_id\":\"hRPaxjlTdR7wFMhV4w0b\"}"'
                    --form
                    'pronunciation_dictionary_locators="{\"pronunciation_dictionary_id\":\"JzWtcGQMJ6bnlWwyMo7e\",\"version_id\":\"lbmwxiLu4q6txYxgdZqn\"}"'.
                callback_url:
                  type:
                    - string
                    - 'null'
                  description: |2-

                        A url that will be called by our service when the Studio project is converted. Request will contain a json blob containing the status of the conversion
                        Messages:
                        1. When project was converted successfully:
                        {
                          type: "project_conversion_status",
                          event_timestamp: 1234567890,
                          data: {
                            request_id: "1234567890",
                            project_id: "21m00Tcm4TlvDq8ikWAM",
                            conversion_status: "success",
                            project_snapshot_id: "22m00Tcm4TlvDq8ikMAT",
                            error_details: None,
                          }
                        }
                        2. When project conversion failed:
                        {
                          type: "project_conversion_status",
                          event_timestamp: 1234567890,
                          data: {
                            request_id: "1234567890",
                            project_id: "21m00Tcm4TlvDq8ikWAM",
                            conversion_status: "error",
                            project_snapshot_id: None,
                            error_details: "Error details if conversion failed"
                          }
                        }

                        3. When chapter was converted successfully:
                        {
                          type: "chapter_conversion_status",
                          event_timestamp: 1234567890,
                          data: {
                            request_id: "1234567890",
                            project_id: "21m00Tcm4TlvDq8ikWAM",
                            chapter_id: "22m00Tcm4TlvDq8ikMAT",
                            conversion_status: "success",
                            chapter_snapshot_id: "23m00Tcm4TlvDq8ikMAV",
                            error_details: None,
                          }
                        }
                        4. When chapter conversion failed:
                        {
                          type: "chapter_conversion_status",
                          event_timestamp: 1234567890,
                          data: {
                            request_id: "1234567890",
                            project_id: "21m00Tcm4TlvDq8ikWAM",
                            chapter_id: "22m00Tcm4TlvDq8ikMAT",
                            conversion_status: "error",
                            chapter_snapshot_id: None,
                            error_details: "Error details if conversion failed"
                          }
                        }
                        
                fiction:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaFiction
                    - type: 'null'
                  description: >-
                    An optional specification of whether the content of this
                    Studio project is fiction.
                apply_text_normalization:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaApplyTextNormalization
                    - type: 'null'
                  description: |2-

                        This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'.
                        When set to 'auto', the system will automatically decide whether to apply text normalization
                        (e.g., spelling out numbers). With 'on', text normalization will always be applied, while
                        with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.
                        
                auto_convert:
                  type: boolean
                  default: false
                  description: Whether to auto convert the Studio project to audio or not.
                auto_assign_voices:
                  type:
                    - boolean
                    - 'null'
                  default: false
                  description: >-
                    [Alpha Feature] Whether automatically assign voices to
                    phrases in the create Project.
                source_type:
                  oneOf:
                    - $ref: >-
                        #/components/schemas/V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaSourceType
                    - type: 'null'
                  description: The type of Studio project to create.
                voice_settings:
                  type: array
                  items:
                    type: string
                  description: |2-
                        Optional voice settings overrides for the project, encoded as a list of JSON strings.

                        Example:
                        ["{\"voice_id\": \"21m00Tcm4TlvDq8ikWAM\", \"stability\": 0.7, \"similarity_boost\": 0.8, \"style\": 0.5, \"speed\": 1.0, \"use_speaker_boost\": true}"]
                        
                create_publishing_read:
                  type:
                    - boolean
                    - 'null'
                  default: false
                  description: >-
                    If true, creates a corresponding read for direct publishing
                    in draft state
              required:
                - name
servers:
  - url: https://api.elevenlabs.io
    description: Production
  - url: https://api.us.elevenlabs.io
    description: Production US
  - url: https://api.eu.residency.elevenlabs.io
    description: Production EU
  - url: https://api.in.residency.elevenlabs.io
    description: Production India
  - url: https://api.sg.residency.elevenlabs.io
    description: Production Singapore
components:
  schemas:
    QualityPresetType:
      type: string
      enum:
        - standard
        - high
        - ultra
        - ultra_lossless
      default: standard
      title: QualityPresetType
    V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaTargetAudience:
      type: string
      enum:
        - children
        - young adult
        - adult
        - all ages
      description: An optional target audience of the Studio project.
      title: >-
        V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaTargetAudience
    V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaFiction:
      type: string
      enum:
        - fiction
        - non-fiction
      description: >-
        An optional specification of whether the content of this Studio project
        is fiction.
      title: V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaFiction
    V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaApplyTextNormalization:
      type: string
      enum:
        - auto
        - 'on'
        - 'off'
        - apply_english
      description: |2-

            This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'.
            When set to 'auto', the system will automatically decide whether to apply text normalization
            (e.g., spelling out numbers). With 'on', text normalization will always be applied, while
            with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.
            
      title: >-
        V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaApplyTextNormalization
    V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaSourceType:
      type: string
      enum:
        - blank
        - book
        - article
        - genfm
        - video
        - screenplay
      description: The type of Studio project to create.
      title: V1StudioProjectsPostRequestBodyContentMultipartFormDataSchemaSourceType
    ProjectResponseModelTargetAudience:
      type: string
      enum:
        - children
        - young adult
        - adult
        - all ages
      description: The target audience of the project.
      title: ProjectResponseModelTargetAudience
    ProjectState:
      type: string
      enum:
        - creating
        - default
        - converting
        - in_queue
      description: The state of the project.
      title: ProjectState
    ProjectResponseModelAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The access level of the project.
      title: ProjectResponseModelAccessLevel
    ProjectResponseModelFiction:
      type: string
      enum:
        - fiction
        - non-fiction
      description: Whether the project is fiction.
      title: ProjectResponseModelFiction
    ProjectCreationMetaResponseModelStatus:
      type: string
      enum:
        - draft
        - pending
        - creating
        - finished
        - failed
      description: The status of the project creation action.
      title: ProjectCreationMetaResponseModelStatus
    ProjectCreationMetaType:
      type: string
      enum:
        - blank
        - generate_podcast
        - auto_assign_voices
        - dub_video
        - import_speech
      title: ProjectCreationMetaType
    ProjectCreationMetaResponseModel:
      type: object
      properties:
        creation_progress:
          type: number
          format: double
          description: The progress of the project creation.
        status:
          $ref: '#/components/schemas/ProjectCreationMetaResponseModelStatus'
          description: The status of the project creation action.
        type:
          $ref: '#/components/schemas/ProjectCreationMetaType'
          description: The type of the project creation action.
      required:
        - creation_progress
        - status
        - type
      title: ProjectCreationMetaResponseModel
    ProjectResponseModelSourceType:
      type: string
      enum:
        - blank
        - book
        - article
        - genfm
        - video
        - screenplay
      description: The source type of the project.
      title: ProjectResponseModelSourceType
    CaptionStyleTemplateModel:
      type: object
      properties:
        key:
          type: string
        label:
          type: string
        requires_high_fps:
          type: boolean
          default: false
      required:
        - key
        - label
      title: CaptionStyleTemplateModel
    CaptionStyleModelTextAlign:
      type: string
      enum:
        - start
        - center
        - end
      title: CaptionStyleModelTextAlign
    CaptionStyleModelTextStyle:
      type: string
      enum:
        - normal
        - italic
      title: CaptionStyleModelTextStyle
    CaptionStyleModelTextWeight:
      type: string
      enum:
        - normal
        - bold
        - '900'
      title: CaptionStyleModelTextWeight
    CaptionStyleModelTextTransform:
      type: string
      enum:
        - none
        - uppercase
      title: CaptionStyleModelTextTransform
    CaptionStyleModelTextBlendMode:
      type: string
      enum:
        - normal
        - difference
        - multiply
      title: CaptionStyleModelTextBlendMode
    StudioTextStyleShadowModel:
      type: object
      properties:
        enabled:
          type: boolean
        color:
          type: string
        opacity:
          type: number
          format: double
        blur:
          type: number
          format: double
        offset_x:
          type: number
          format: double
        offset_y:
          type: number
          format: double
      required:
        - enabled
        - color
        - opacity
        - blur
        - offset_x
        - offset_y
      title: StudioTextStyleShadowModel
    StudioTextStyleOutlineModel:
      type: object
      properties:
        enabled:
          type: boolean
        color:
          type: string
        opacity:
          type: number
          format: double
        width:
          type: number
          format: double
      required:
        - enabled
        - color
        - opacity
        - width
      title: StudioTextStyleOutlineModel
    CaptionStyleSectionAnimationModelEnterType:
      type: string
      enum:
        - none
        - fade
        - scale
        - pop
        - slide_up
        - slide_down
        - slam
        - scale_down
        - slide_in
      title: CaptionStyleSectionAnimationModelEnterType
    CaptionStyleSectionAnimationModelExitType:
      type: string
      enum:
        - none
        - fade
        - scale
        - pop
        - slide_up
        - slide_down
        - slam
        - scale_down
        - slide_in
      title: CaptionStyleSectionAnimationModelExitType
    CaptionStyleSectionAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleSectionAnimationModelExitType'
      required:
        - enter_type
        - exit_type
      title: CaptionStyleSectionAnimationModel
    CaptionStyleWordAnimationModelEnterType:
      type: string
      enum:
        - none
        - fade
        - scale
        - pop
        - slide_up
        - slide_down
        - slam
        - scale_down
        - slide_in
      title: CaptionStyleWordAnimationModelEnterType
    CaptionStyleWordAnimationModelExitType:
      type: string
      enum:
        - none
        - fade
        - scale
        - pop
        - slide_up
        - slide_down
        - slam
        - scale_down
        - slide_in
      title: CaptionStyleWordAnimationModelExitType
    CaptionStyleWordAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleWordAnimationModelExitType'
      required:
        - enter_type
        - exit_type
      title: CaptionStyleWordAnimationModel
    CaptionStyleCharacterAnimationModelEnterType:
      type: string
      enum:
        - none
        - fade
        - typewriter
      title: CaptionStyleCharacterAnimationModelEnterType
    CaptionStyleCharacterAnimationModelExitType:
      type: string
      enum:
        - none
        - fade
      title: CaptionStyleCharacterAnimationModelExitType
    CaptionStyleCharacterAnimationModel:
      type: object
      properties:
        enter_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelEnterType'
        exit_type:
          $ref: '#/components/schemas/CaptionStyleCharacterAnimationModelExitType'
      required:
        - enter_type
        - exit_type
      title: CaptionStyleCharacterAnimationModel
    CaptionStyleHorizontalPlacementModelAlign:
      type: string
      enum:
        - left
        - center
        - right
      title: CaptionStyleHorizontalPlacementModelAlign
    CaptionStyleHorizontalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
      title: CaptionStyleHorizontalPlacementModel
    CaptionStyleVerticalPlacementModelAlign:
      type: string
      enum:
        - top
        - center
        - bottom
      title: CaptionStyleVerticalPlacementModelAlign
    CaptionStyleVerticalPlacementModel:
      type: object
      properties:
        align:
          $ref: '#/components/schemas/CaptionStyleVerticalPlacementModelAlign'
        translate_pct:
          type: number
          format: double
      required:
        - align
        - translate_pct
      title: CaptionStyleVerticalPlacementModel
    CaptionStyleModel:
      type: object
      properties:
        template:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleTemplateModel'
            - type: 'null'
        text_font:
          type:
            - string
            - 'null'
        text_scale:
          type:
            - number
            - 'null'
          format: double
        text_color:
          type:
            - string
            - 'null'
        text_align:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextAlign'
            - type: 'null'
        text_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextStyle'
            - type: 'null'
        text_weight:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextWeight'
            - type: 'null'
        text_transform:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextTransform'
            - type: 'null'
        text_blend_mode:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModelTextBlendMode'
            - type: 'null'
        text_shadow:
          oneOf:
            - $ref: '#/components/schemas/StudioTextStyleShadowModel'
            - type: 'null'
        text_outline:
          oneOf:
            - $ref: '#/components/schemas/StudioTextStyleOutlineModel'
            - type: 'null'
        background_enabled:
          type:
            - boolean
            - 'null'
        background_color:
          type:
            - string
            - 'null'
        background_opacity:
          type:
            - number
            - 'null'
          format: double
        background_blur:
          type:
            - number
            - 'null'
          format: double
        background_border_radius:
          type:
            - number
            - 'null'
          format: double
        word_highlights_enabled:
          type:
            - boolean
            - 'null'
        word_highlights_color:
          type:
            - string
            - 'null'
        word_highlights_background_color:
          type:
            - string
            - 'null'
        word_highlights_opacity:
          type:
            - number
            - 'null'
          format: double
        word_highlights_border_radius:
          type:
            - number
            - 'null'
          format: double
        word_highlights_blur:
          type:
            - number
            - 'null'
          format: double
        section_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleSectionAnimationModel'
            - type: 'null'
        word_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleWordAnimationModel'
            - type: 'null'
        character_animation:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleCharacterAnimationModel'
            - type: 'null'
        cursor_enabled:
          type:
            - boolean
            - 'null'
        width_pct:
          type:
            - number
            - 'null'
          format: double
        horizontal_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleHorizontalPlacementModel'
            - type: 'null'
        vertical_placement:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleVerticalPlacementModel'
            - type: 'null'
        auto_break_enabled:
          type:
            - boolean
            - 'null'
        max_lines_per_section:
          type:
            - integer
            - 'null'
        max_words_per_line:
          type:
            - integer
            - 'null'
      title: CaptionStyleModel
    ProjectResponseModelAspectRatio:
      type: string
      enum:
        - '16:9'
        - '9:16'
        - '4:5'
        - '1:1'
      description: The aspect ratio of the project.
      title: ProjectResponseModelAspectRatio
    StudioAgentToolSettingsModel:
      type: object
      properties:
        skip_confirmation:
          type: boolean
          default: false
      title: StudioAgentToolSettingsModel
    StudioAgentSettingsModel:
      type: object
      properties:
        tool_settings:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/StudioAgentToolSettingsModel'
      title: StudioAgentSettingsModel
    ProjectResponseModel:
      type: object
      properties:
        project_id:
          type: string
          description: The ID of the project.
        name:
          type: string
          description: The name of the project.
        create_date_unix:
          type: integer
          description: The creation date of the project.
        created_by_user_id:
          type:
            - string
            - 'null'
          description: The user ID who created the project.
        default_title_voice_ref_id:
          type: string
          description: The default title project voice reference ID.
        default_paragraph_voice_ref_id:
          type: string
          description: The default paragraph project voice reference ID.
        default_model_id:
          type: string
          description: The default model ID.
        last_conversion_date_unix:
          type:
            - integer
            - 'null'
          description: The last conversion date of the project.
        can_be_downloaded:
          type: boolean
          description: Whether the project can be downloaded.
        title:
          type:
            - string
            - 'null'
          description: The title of the project.
        author:
          type:
            - string
            - 'null'
          description: The author of the project.
        description:
          type:
            - string
            - 'null'
          description: The description of the project.
        genres:
          type:
            - array
            - 'null'
          items:
            type: string
          description: List of genres of the project.
        cover_image_url:
          type:
            - string
            - 'null'
          description: The cover image URL of the project.
        target_audience:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelTargetAudience'
            - type: 'null'
          description: The target audience of the project.
        language:
          type:
            - string
            - 'null'
          description: Two-letter language code (ISO 639-1) of the language of the project.
        content_type:
          type:
            - string
            - 'null'
          description: The content type of the project, e.g. 'Novel' or 'Short Story'
        original_publication_date:
          type:
            - string
            - 'null'
          description: The original publication date of the project.
        mature_content:
          type:
            - boolean
            - 'null'
          description: Whether the project contains mature content.
        isbn_number:
          type:
            - string
            - 'null'
          description: The ISBN number of the project.
        volume_normalization:
          type: boolean
          description: Whether the project uses volume normalization.
        state:
          $ref: '#/components/schemas/ProjectState'
          description: The state of the project.
        access_level:
          $ref: '#/components/schemas/ProjectResponseModelAccessLevel'
          description: The access level of the project.
        fiction:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelFiction'
            - type: 'null'
          description: Whether the project is fiction.
        quality_check_on:
          type: boolean
          description: Whether quality check is enabled for this project.
        quality_check_on_when_bulk_convert:
          type: boolean
          description: >-
            Whether quality check is enabled on the project when bulk
            converting.
        creation_meta:
          oneOf:
            - $ref: '#/components/schemas/ProjectCreationMetaResponseModel'
            - type: 'null'
          description: The creation meta of the project.
        source_type:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelSourceType'
            - type: 'null'
          description: The source type of the project.
        chapters_enabled:
          type:
            - boolean
            - 'null'
          default: true
          description: Whether chapters are enabled for the project.
        captions_enabled:
          type:
            - boolean
            - 'null'
          default: true
          description: Whether captions are enabled for the project.
        caption_style:
          oneOf:
            - $ref: '#/components/schemas/CaptionStyleModel'
            - type: 'null'
          description: Global styling to be applied to all captions
        caption_style_template_overrides:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/CaptionStyleModel'
          description: Styling changes that have been made to the provided templates
        public_share_id:
          type:
            - string
            - 'null'
          description: The public share ID of the project.
        aspect_ratio:
          oneOf:
            - $ref: '#/components/schemas/ProjectResponseModelAspectRatio'
            - type: 'null'
          description: The aspect ratio of the project.
        agent_settings:
          oneOf:
            - $ref: '#/components/schemas/StudioAgentSettingsModel'
            - type: 'null'
          description: Agent-related settings for the project
        default_title_voice_id:
          type: string
          description: The default title voice ID.
        default_paragraph_voice_id:
          type: string
          description: The default paragraph voice ID.
      required:
        - project_id
        - name
        - create_date_unix
        - created_by_user_id
        - default_title_voice_ref_id
        - default_paragraph_voice_ref_id
        - default_model_id
        - can_be_downloaded
        - volume_normalization
        - state
        - access_level
        - quality_check_on
        - quality_check_on_when_bulk_convert
        - default_title_voice_id
        - default_paragraph_voice_id
      title: ProjectResponseModel
    AddProjectResponseModel:
      type: object
      properties:
        project:
          $ref: '#/components/schemas/ProjectResponseModel'
      required:
        - project
      title: AddProjectResponseModel
    ValidationErrorLocItems:
      oneOf:
        - type: string
        - type: integer
      title: ValidationErrorLocItems
    ValidationError:
      type: object
      properties:
        loc:
          type: array
          items:
            $ref: '#/components/schemas/ValidationErrorLocItems'
        msg:
          type: string
        type:
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
    HTTPValidationError:
      type: object
      properties:
        detail:
          type: array
          items:
            $ref: '#/components/schemas/ValidationError'
      title: HTTPValidationError

```

## Examples



**Request**

```json
{
  "from_document": "<file: <file1>>",
  "name": "Project 1"
}
```

**Response**

```json
{
  "project": {
    "project_id": "aw1NgEzBg83R7vgmiJt6",
    "name": "My Project",
    "create_date_unix": 1714204800,
    "created_by_user_id": "Vbtgl3bRdj6lk79rYAgx",
    "default_title_voice_ref_id": "JBFqnCBsd6RMkjVDRZzb",
    "default_paragraph_voice_ref_id": "JBFqnCBsd6RMkjVDRZzb",
    "default_model_id": "eleven_multilingual_v2",
    "can_be_downloaded": true,
    "volume_normalization": true,
    "state": "default",
    "access_level": "viewer",
    "quality_check_on": false,
    "quality_check_on_when_bulk_convert": false,
    "default_title_voice_id": "JBFqnCBsd6RMkjVDRZzb",
    "default_paragraph_voice_id": "JBFqnCBsd6RMkjVDRZzb",
    "last_conversion_date_unix": 1714204800,
    "title": "My Project",
    "author": "John Doe",
    "description": "This is a description of my project.",
    "genres": [
      "Novel",
      "Short Story"
    ],
    "cover_image_url": "https://example.com/cover.jpg",
    "target_audience": "young adult",
    "language": "en",
    "content_type": "Novel",
    "original_publication_date": "2025-01-01",
    "mature_content": false,
    "isbn_number": "978-90-274-3964-2",
    "fiction": "fiction",
    "creation_meta": {
      "creation_progress": 0.5,
      "status": "pending",
      "type": "blank"
    },
    "public_share_id": "abc123def456789"
  }
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.create({});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.create(
    from_document="example_from_document",
)

```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"create_publishing_read\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.elevenlabs.io/v1/studio/projects")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"create_publishing_read\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/projects")
  .header("Content-Type", "multipart/form-data; boundary=---011000010111000001101001")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"create_publishing_read\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/projects', [
  'multipart' => [
    [
        'name' => 'from_document',
        'filename' => '<file1>',
        'contents' => null
    ],
    [
        'name' => 'name',
        'contents' => 'Project 1'
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects");
var request = new RestRequest(Method.POST);
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"acx_volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"apply_text_normalization\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"author\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_assign_voices\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"auto_convert\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"callback_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"create_publishing_read\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_model_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_paragraph_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"default_title_voice_id\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fiction\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_content_json\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_document\"; filename=\"<file1>\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"from_url\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"genres\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"isbn_number\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mature_content\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\nProject 1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"original_publication_date\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pronunciation_dictionary_locators\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"quality_preset\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"source_type\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"target_audience\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"voice_settings\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"volume_normalization\"\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "multipart/form-data; boundary=---011000010111000001101001"]
let parameters = [
  [
    "name": "acx_volume_normalization",
    "value": 
  ],
  [
    "name": "apply_text_normalization",
    "value": 
  ],
  [
    "name": "author",
    "value": 
  ],
  [
    "name": "auto_assign_voices",
    "value": 
  ],
  [
    "name": "auto_convert",
    "value": 
  ],
  [
    "name": "callback_url",
    "value": 
  ],
  [
    "name": "content_type",
    "value": 
  ],
  [
    "name": "create_publishing_read",
    "value": 
  ],
  [
    "name": "default_model_id",
    "value": 
  ],
  [
    "name": "default_paragraph_voice_id",
    "value": 
  ],
  [
    "name": "default_title_voice_id",
    "value": 
  ],
  [
    "name": "description",
    "value": 
  ],
  [
    "name": "fiction",
    "value": 
  ],
  [
    "name": "from_content_json",
    "value": 
  ],
  [
    "name": "from_document",
    "fileName": "<file1>"
  ],
  [
    "name": "from_url",
    "value": 
  ],
  [
    "name": "genres",
    "value": 
  ],
  [
    "name": "isbn_number",
    "value": 
  ],
  [
    "name": "language",
    "value": 
  ],
  [
    "name": "mature_content",
    "value": 
  ],
  [
    "name": "name",
    "value": "Project 1"
  ],
  [
    "name": "original_publication_date",
    "value": 
  ],
  [
    "name": "pronunciation_dictionary_locators",
    "value": 
  ],
  [
    "name": "quality_preset",
    "value": 
  ],
  [
    "name": "source_type",
    "value": 
  ],
  [
    "name": "target_audience",
    "value": 
  ],
  [
    "name": "title",
    "value": 
  ],
  [
    "name": "voice_settings",
    "value": 
  ],
  [
    "name": "volume_normalization",
    "value": 
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
