---
title: "Get Studio Project"
source: https://elevenlabs.io/docs/api-reference/studio/get-project.md
path: docs/api-reference/studio/get-project
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Get Studio Project

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}

Returns information about a specific Studio project. This endpoint returns more detailed information about a project than `GET /v1/studio`.

Reference: https://elevenlabs.io/docs/api-reference/studio/get-project

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/studio/projects/{project_id}:
    get:
      operationId: get
      summary: Get Studio Project
      description: >-
        Returns information about a specific Studio project. This endpoint
        returns more detailed information about a project than `GET /v1/studio`.
      tags:
        - projects
      parameters:
        - name: project_id
          in: path
          description: >-
            The ID of the project to be used. You can use the [List
            projects](/docs/api-reference/studio/get-projects) endpoint to list
            all the available projects.
          required: true
          schema:
            type: string
        - name: share_id
          in: query
          description: The share ID of the project
          required: false
          schema:
            type:
              - string
              - 'null'
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
                $ref: '#/components/schemas/ProjectExtendedResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
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
    ProjectExtendedResponseModelTargetAudience:
      type: string
      enum:
        - children
        - young adult
        - adult
        - all ages
      description: The target audience of the project.
      title: ProjectExtendedResponseModelTargetAudience
    ProjectState:
      type: string
      enum:
        - creating
        - default
        - converting
        - in_queue
      description: The state of the project.
      title: ProjectState
    ProjectExtendedResponseModelAccessLevel:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      description: The access level of the project.
      title: ProjectExtendedResponseModelAccessLevel
    ProjectExtendedResponseModelFiction:
      type: string
      enum:
        - fiction
        - non-fiction
      description: Whether the project is fiction.
      title: ProjectExtendedResponseModelFiction
    ProjectCreationMetaResponseModelStatus:
      type: string
      enum:
        - pending
        - creating
        - finished
        - failed
      description: The status of the project creation action.
      title: ProjectCreationMetaResponseModelStatus
    ProjectCreationMetaResponseModelType:
      type: string
      enum:
        - blank
        - generate_podcast
        - auto_assign_voices
        - dub_video
        - import_speech
      description: The type of the project creation action.
      title: ProjectCreationMetaResponseModelType
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
          $ref: '#/components/schemas/ProjectCreationMetaResponseModelType'
          description: The type of the project creation action.
      required:
        - creation_progress
        - status
        - type
      title: ProjectCreationMetaResponseModel
    ProjectExtendedResponseModelSourceType:
      type: string
      enum:
        - blank
        - book
        - article
        - genfm
        - video
        - screenplay
      description: The source type of the project.
      title: ProjectExtendedResponseModelSourceType
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
    ProjectExtendedResponseModelAspectRatio:
      type: string
      enum:
        - '16:9'
        - '9:16'
        - '4:5'
        - '1:1'
      description: The aspect ratio of the project.
      title: ProjectExtendedResponseModelAspectRatio
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
    QualityPresetType:
      type: string
      enum:
        - standard
        - high
        - ultra
        - ultra_lossless
      default: standard
      title: QualityPresetType
    ChapterState:
      type: string
      enum:
        - default
        - converting
      description: The state of the chapter.
      title: ChapterState
    VoiceStatisticsResponseModel:
      type: object
      properties:
        project_voice_ref_id:
          type: string
          description: The project voice reference ID.
        characters_unconverted:
          type: integer
          description: The number of unconverted characters for this voice.
        characters_converted:
          type: integer
          description: The number of converted characters for this voice.
        credits_needed_to_convert:
          type:
            - integer
            - 'null'
          description: >-
            The number of credits needed to convert the remaining audio for this
            voice.
        voice_id:
          type: string
          description: The voice ID.
      required:
        - project_voice_ref_id
        - characters_unconverted
        - characters_converted
        - voice_id
      title: VoiceStatisticsResponseModel
    ChapterStatisticsResponseModel:
      type: object
      properties:
        characters_unconverted:
          type: integer
          description: The number of unconverted characters.
        characters_converted:
          type: integer
          description: The number of converted characters.
        paragraphs_converted:
          type: integer
          description: The number of converted paragraphs.
        paragraphs_unconverted:
          type: integer
          description: The number of unconverted paragraphs.
        credits_needed_to_convert:
          type:
            - integer
            - 'null'
          description: The number of credits needed to convert the remaining paragraphs.
        voice_statistics:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VoiceStatisticsResponseModel'
          description: Per-voice breakdown of character counts.
      required:
        - characters_unconverted
        - characters_converted
        - paragraphs_converted
        - paragraphs_unconverted
      title: ChapterStatisticsResponseModel
    ChapterResponseModel:
      type: object
      properties:
        chapter_id:
          type: string
          description: The ID of the chapter.
        name:
          type: string
          description: The name of the chapter.
        last_conversion_date_unix:
          type:
            - integer
            - 'null'
          description: The last conversion date of the chapter.
        conversion_progress:
          type:
            - number
            - 'null'
          format: double
          description: The conversion progress of the chapter.
        can_be_downloaded:
          type: boolean
          description: Whether the chapter can be downloaded.
        state:
          $ref: '#/components/schemas/ChapterState'
          description: The state of the chapter.
        has_video:
          type:
            - boolean
            - 'null'
          description: Whether the chapter has a video.
        has_visual_content:
          type:
            - boolean
            - 'null'
          description: >-
            Whether the chapter has any visual content (video, image, or text
            clips).
        voice_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: List of voice ids used by the chapter
        statistics:
          oneOf:
            - $ref: '#/components/schemas/ChapterStatisticsResponseModel'
            - type: 'null'
          description: The statistics of the chapter.
        last_conversion_error:
          type:
            - string
            - 'null'
          description: The last conversion error of the chapter.
      required:
        - chapter_id
        - name
        - can_be_downloaded
        - state
      title: ChapterResponseModel
    PronunciationDictionaryVersionResponseModelPermissionOnResource:
      type: string
      enum:
        - admin
        - editor
        - commenter
        - viewer
      title: PronunciationDictionaryVersionResponseModelPermissionOnResource
    PronunciationDictionaryVersionResponseModel:
      type: object
      properties:
        version_id:
          type: string
        version_rules_num:
          type: integer
        pronunciation_dictionary_id:
          type: string
        dictionary_name:
          type: string
        version_name:
          type: string
        permission_on_resource:
          oneOf:
            - $ref: >-
                #/components/schemas/PronunciationDictionaryVersionResponseModelPermissionOnResource
            - type: 'null'
        created_by:
          type: string
        creation_time_unix:
          type: integer
        archived_time_unix:
          type:
            - integer
            - 'null'
      required:
        - version_id
        - version_rules_num
        - pronunciation_dictionary_id
        - dictionary_name
        - version_name
        - permission_on_resource
        - created_by
        - creation_time_unix
      title: PronunciationDictionaryVersionResponseModel
    PronunciationDictionaryLocatorResponseModel:
      type: object
      properties:
        pronunciation_dictionary_id:
          type: string
        version_id:
          type:
            - string
            - 'null'
      required:
        - pronunciation_dictionary_id
        - version_id
      title: PronunciationDictionaryLocatorResponseModel
    ProjectExtendedResponseModelApplyTextNormalization:
      type: string
      enum:
        - auto
        - 'on'
        - 'off'
        - apply_english
      description: Whether text normalization is applied to the project.
      title: ProjectExtendedResponseModelApplyTextNormalization
    ProjectVideoThumbnailSheetResponseModel:
      type: object
      properties:
        start_thumbnail_index:
          type: integer
        thumbnail_count:
          type: integer
        signed_cloud_url:
          type: string
      required:
        - start_thumbnail_index
        - thumbnail_count
        - signed_cloud_url
      title: ProjectVideoThumbnailSheetResponseModel
    PendingBlocksMetadataModel:
      type: object
      properties:
        target_global_offset_ms:
          type:
            - integer
            - 'null'
        block_ids:
          type: array
          items:
            type: string
      required:
        - target_global_offset_ms
        - block_ids
      title: PendingBlocksMetadataModel
    PendingExternalAudiosMetadataModel:
      type: object
      properties:
        target_global_offset_ms:
          type:
            - integer
            - 'null'
        external_audio_ids:
          type: array
          items:
            type: string
      required:
        - target_global_offset_ms
        - external_audio_ids
      title: PendingExternalAudiosMetadataModel
    PendingClipTaskType:
      type: string
      enum:
        - preprocessing
        - speech_import
        - dubbing
        - video_to_music
        - media_generation
      title: PendingClipTaskType
    PendingClipTask:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/PendingClipTaskType'
        progress:
          type: number
          format: double
          default: 0
        started_at_ms:
          type: integer
        updated_at_ms:
          type: integer
        metadata:
          type: object
          additionalProperties:
            description: Any type
      required:
        - type
      title: PendingClipTask
    StudioClipReferenceClipType:
      type: string
      enum:
        - video
        - image
        - external_audio
        - tts_node
      title: StudioClipReferenceClipType
    StudioClipReference:
      type: object
      properties:
        project_id:
          type: string
        chapter_id:
          type: string
        clip_type:
          $ref: '#/components/schemas/StudioClipReferenceClipType'
        clip_id:
          type: string
        block_id:
          type:
            - string
            - 'null'
        preview_url:
          type:
            - string
            - 'null'
      required:
        - project_id
        - chapter_id
        - clip_type
        - clip_id
      title: StudioClipReference
    ReferenceVideo:
      type: object
      properties:
        generation_id:
          type:
            - string
            - 'null'
        content_asset_id:
          type:
            - string
            - 'null'
        template_node_id:
          type:
            - string
            - 'null'
        studio_clip:
          oneOf:
            - $ref: '#/components/schemas/StudioClipReference'
            - type: 'null'
      title: ReferenceVideo
    GenerationSourceContext:
      type: object
      properties:
        source_type:
          type: string
          enum:
            - generation
          default: generation
        generation_id:
          type: string
        prompt:
          type:
            - string
            - 'null'
        model_id:
          type: string
        model_provider:
          type:
            - string
            - 'null'
        generation_session_id:
          type:
            - string
            - 'null'
        session_iteration_id:
          type:
            - string
            - 'null'
        model_parameters:
          type:
            - object
            - 'null'
          additionalProperties:
            description: Any type
        extend_video:
          oneOf:
            - $ref: '#/components/schemas/ReferenceVideo'
            - type: 'null'
      required:
        - generation_id
        - model_id
      title: GenerationSourceContext
    VideoAnalysisStatus:
      type: string
      enum:
        - processing
        - completed
        - failed
      title: VideoAnalysisStatus
    VideoSubject:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
      required:
        - name
        - description
      title: VideoSubject
    VideoSegment:
      type: object
      properties:
        start_ms:
          type: integer
        end_ms:
          type: integer
        description:
          type: string
        subjects:
          type: array
          items:
            type: string
        shot_type:
          type:
            - string
            - 'null'
        camera_movement:
          type:
            - string
            - 'null'
        transition_in:
          type:
            - string
            - 'null'
        has_speech:
          type: boolean
          default: false
        has_music:
          type: boolean
          default: false
        pacing:
          type:
            - string
            - 'null'
      required:
        - start_ms
        - end_ms
        - description
      title: VideoSegment
    VideoKeyMoment:
      type: object
      properties:
        timestamp_ms:
          type: integer
        type:
          type: string
        description:
          type: string
      required:
        - timestamp_ms
        - type
        - description
      title: VideoKeyMoment
    VideoAnalysisResult:
      type: object
      properties:
        title:
          type: string
        description:
          type: string
        content_type:
          type:
            - string
            - 'null'
        overall_pacing:
          type:
            - string
            - 'null'
        subjects:
          type: array
          items:
            $ref: '#/components/schemas/VideoSubject'
        segments:
          type: array
          items:
            $ref: '#/components/schemas/VideoSegment'
        key_moments:
          type: array
          items:
            $ref: '#/components/schemas/VideoKeyMoment'
      required:
        - title
        - description
      title: VideoAnalysisResult
    VideoAnalysis:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/VideoAnalysisStatus'
        data:
          oneOf:
            - $ref: '#/components/schemas/VideoAnalysisResult'
            - type: 'null'
        updated_at_ms:
          type: integer
      required:
        - status
        - data
      title: VideoAnalysis
    AssetTranscriptionStatus:
      type: string
      enum:
        - processing
        - completed
        - failed
      title: AssetTranscriptionStatus
    AssetTranscriptionData:
      type: object
      properties:
        language_code:
          type: string
        text:
          type: string
        words:
          type: array
          items:
            type: string
        word_start_times_ms:
          type: array
          items:
            type: integer
        word_end_times_ms:
          type: array
          items:
            type: integer
        word_speaker_ids:
          type: array
          items:
            type:
              - string
              - 'null'
      required:
        - language_code
        - text
        - words
        - word_start_times_ms
        - word_end_times_ms
        - word_speaker_ids
      title: AssetTranscriptionData
    AssetTranscription:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/AssetTranscriptionStatus'
        data:
          oneOf:
            - $ref: '#/components/schemas/AssetTranscriptionData'
            - type: 'null'
        updated_at_ms:
          type: integer
      required:
        - status
        - data
      title: AssetTranscription
    CanvasPlacement:
      type: object
      properties:
        x_relative:
          type: number
          format: double
          default: 0.5
        y_relative:
          type: number
          format: double
          default: 0.5
        scale_x:
          type: number
          format: double
          default: 1
        scale_y:
          type: number
          format: double
          default: 1
        pivot_x:
          type: number
          format: double
          default: 0
        pivot_y:
          type: number
          format: double
          default: 0
        skew_x:
          type: number
          format: double
          default: 0
        skew_y:
          type: number
          format: double
          default: 0
        crop_top:
          type: number
          format: double
          default: 0
        crop_right:
          type: number
          format: double
          default: 0
        crop_bottom:
          type: number
          format: double
          default: 0
        crop_left:
          type: number
          format: double
          default: 0
        flip_x:
          type: boolean
          default: false
        flip_y:
          type: boolean
          default: false
      description: Defines asset positioning and transformation on canvas.
      title: CanvasPlacement
    ClipAnimationEnterEffect:
      type: string
      enum:
        - none
        - fade
        - float
        - gentle_float
        - zoom_in
        - drop
        - slide_left
        - slide_right
        - slide_up
        - slide_down
        - pop
        - bounce
        - spin
        - slide_bounce
      default: none
      title: ClipAnimationEnterEffect
    ClipAnimationExitEffect:
      type: string
      enum:
        - none
        - fade
        - float
        - gentle_float
        - zoom_in
        - drop
        - slide_left
        - slide_right
        - slide_up
        - slide_down
        - pop
        - bounce
        - spin
        - slide_bounce
      default: none
      title: ClipAnimationExitEffect
    ClipAnimation:
      type: object
      properties:
        enter_effect:
          $ref: '#/components/schemas/ClipAnimationEnterEffect'
          default: none
        enter_duration_ms:
          type: integer
          default: 0
        exit_effect:
          $ref: '#/components/schemas/ClipAnimationExitEffect'
          default: none
        exit_duration_ms:
          type: integer
          default: 0
      title: ClipAnimation
    ProjectVideoResponseModel:
      type: object
      properties:
        video_id:
          type: string
        filename:
          type: string
        signed_url:
          type:
            - string
            - 'null'
        signed_preview_url:
          type:
            - string
            - 'null'
        offset_ms:
          type: integer
        duration_ms:
          type: integer
        volume_gain_db:
          type: number
          format: double
        muted:
          type: boolean
        fade_in_ms:
          type: integer
          default: 0
        fade_out_ms:
          type: integer
          default: 0
        width:
          type: integer
        height:
          type: integer
        codec:
          type: string
        order:
          type: string
        created_at_ms:
          type: integer
        updated_at_ms:
          type: integer
        error:
          type:
            - string
            - 'null'
        thumbnail_interval_seconds:
          type: number
          format: double
        thumbnail_size:
          type: array
          items:
            type: integer
        thumbnail_sheets:
          type: array
          items:
            $ref: '#/components/schemas/ProjectVideoThumbnailSheetResponseModel'
        start_time_ms:
          type: integer
        end_time_ms:
          type:
            - integer
            - 'null'
        asset_preview_signed_url:
          type:
            - string
            - 'null'
        source_video_id:
          type:
            - string
            - 'null'
        source_asset_id:
          type:
            - string
            - 'null'
        source_platform_asset_id:
          type:
            - string
            - 'null'
        pending_blocks_metadata:
          oneOf:
            - $ref: '#/components/schemas/PendingBlocksMetadataModel'
            - type: 'null'
        pending_external_audios_metadata:
          oneOf:
            - $ref: '#/components/schemas/PendingExternalAudiosMetadataModel'
            - type: 'null'
        speech_imported:
          type: boolean
          default: false
        pending_task:
          oneOf:
            - $ref: '#/components/schemas/PendingClipTask'
            - type: 'null'
        audio_track_ready:
          type: boolean
          default: true
        export_format_ready:
          type: boolean
          default: true
        current_snapshot_id:
          type:
            - string
            - 'null'
        source_context:
          oneOf:
            - $ref: '#/components/schemas/GenerationSourceContext'
            - type: 'null'
        analysis:
          oneOf:
            - $ref: '#/components/schemas/VideoAnalysis'
            - type: 'null'
        transcription:
          oneOf:
            - $ref: '#/components/schemas/AssetTranscription'
            - type: 'null'
        type:
          type: string
          enum:
            - video
          default: video
        canvas_placement:
          $ref: '#/components/schemas/CanvasPlacement'
        animation:
          $ref: '#/components/schemas/ClipAnimation'
        playback_speed:
          type: number
          format: double
          default: 1
        opacity:
          type: number
          format: double
          default: 1
        track_id:
          type: string
          default: v0
        preview_job_progress:
          type: number
          format: double
        import_speech_progress:
          type:
            - number
            - 'null'
          format: double
      required:
        - video_id
        - filename
        - signed_url
        - signed_preview_url
        - offset_ms
        - duration_ms
        - volume_gain_db
        - muted
        - width
        - height
        - codec
        - order
        - created_at_ms
        - updated_at_ms
        - thumbnail_interval_seconds
        - thumbnail_size
        - thumbnail_sheets
        - start_time_ms
        - end_time_ms
        - preview_job_progress
        - import_speech_progress
      title: ProjectVideoResponseModel
    ProjectExternalAudioResponseModelSourceContext:
      oneOf:
        - type: object
          properties:
            source_type:
              type: string
              enum:
                - music_explore_song
              description: 'Discriminator value: music_explore_song'
            music_explore_song_id:
              type: string
            title:
              type:
                - string
                - 'null'
            description:
              type:
                - string
                - 'null'
            bpm:
              type:
                - integer
                - 'null'
            vocals:
              type:
                - string
                - 'null'
            lyrics:
              type:
                - string
                - 'null'
          required:
            - source_type
            - music_explore_song_id
          description: MusicExploreSongSourceContext variant
        - type: object
          properties:
            source_type:
              type: string
              enum:
                - sfx
              default: sfx
            sound_generation_history_item_id:
              type:
                - string
                - 'null'
            text:
              type:
                - string
                - 'null'
            generation_config:
              type:
                - object
                - 'null'
              additionalProperties:
                description: Any type
          required:
            - source_type
          description: Context for sound effect clips.
        - type: object
          properties:
            source_type:
              type: string
              enum:
                - song
              default: song
            song_id:
              type: string
            chat_id:
              type:
                - string
                - 'null'
            title:
              type:
                - string
                - 'null'
            description:
              type:
                - string
                - 'null'
            genres:
              type: array
              items:
                type: string
            languages:
              type: array
              items:
                type: string
            is_explicit:
              type:
                - boolean
                - 'null'
            bpm:
              type:
                - integer
                - 'null'
            generation_settings:
              type:
                - object
                - 'null'
              additionalProperties:
                description: Any type
          required:
            - source_type
            - song_id
          description: SongSourceContext variant
      discriminator:
        propertyName: source_type
      title: ProjectExternalAudioResponseModelSourceContext
    AudioAnalysisStatus:
      type: string
      enum:
        - processing
        - completed
        - failed
      title: AudioAnalysisStatus
    AudioSegment:
      type: object
      properties:
        start_ms:
          type: integer
        end_ms:
          type: integer
        description:
          type: string
        segment_type:
          type:
            - string
            - 'null'
        has_speech:
          type: boolean
          default: false
        has_music:
          type: boolean
          default: false
        pacing:
          type:
            - string
            - 'null'
      required:
        - start_ms
        - end_ms
        - description
      title: AudioSegment
    AudioKeyMoment:
      type: object
      properties:
        timestamp_ms:
          type: integer
        type:
          type: string
        description:
          type: string
      required:
        - timestamp_ms
        - type
        - description
      title: AudioKeyMoment
    AudioAnalysisResult:
      type: object
      properties:
        title:
          type: string
        description:
          type: string
        content_type:
          type:
            - string
            - 'null'
        overall_pacing:
          type:
            - string
            - 'null'
        segments:
          type: array
          items:
            $ref: '#/components/schemas/AudioSegment'
        key_moments:
          type: array
          items:
            $ref: '#/components/schemas/AudioKeyMoment'
      required:
        - title
        - description
      title: AudioAnalysisResult
    AudioAnalysis:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/AudioAnalysisStatus'
        data:
          oneOf:
            - $ref: '#/components/schemas/AudioAnalysisResult'
            - type: 'null'
        updated_at_ms:
          type: integer
      required:
        - status
        - data
      title: AudioAnalysis
    ProjectExternalAudioResponseModel:
      type: object
      properties:
        external_audio_id:
          type: string
        filename:
          type: string
        signed_url:
          type:
            - string
            - 'null'
        offset_ms:
          type: integer
        duration_ms:
          type: integer
        start_time_ms:
          type: integer
        end_time_ms:
          type:
            - integer
            - 'null'
        order:
          type: string
        track_id:
          type: string
        created_at_ms:
          type: integer
        updated_at_ms:
          type: integer
        volume_gain_db:
          type: number
          format: double
          default: 0
        muted:
          type: boolean
          default: false
        fade_in_ms:
          type: integer
          default: 0
        fade_out_ms:
          type: integer
          default: 0
        source_external_audio_id:
          type:
            - string
            - 'null'
        source_asset_id:
          type:
            - string
            - 'null'
        source_platform_asset_id:
          type:
            - string
            - 'null'
        pending_blocks_metadata:
          oneOf:
            - $ref: '#/components/schemas/PendingBlocksMetadataModel'
            - type: 'null'
        pending_external_audios_metadata:
          oneOf:
            - $ref: '#/components/schemas/PendingExternalAudiosMetadataModel'
            - type: 'null'
        speech_imported:
          type: boolean
          default: false
        pending_task:
          oneOf:
            - $ref: '#/components/schemas/PendingClipTask'
            - type: 'null'
        error:
          type:
            - string
            - 'null'
        current_snapshot_id:
          type:
            - string
            - 'null'
        source_context:
          oneOf:
            - $ref: >-
                #/components/schemas/ProjectExternalAudioResponseModelSourceContext
            - type: 'null'
        analysis:
          oneOf:
            - $ref: '#/components/schemas/AudioAnalysis'
            - type: 'null'
        transcription:
          oneOf:
            - $ref: '#/components/schemas/AssetTranscription'
            - type: 'null'
        type:
          type: string
          enum:
            - audio
          default: audio
        import_speech_progress:
          type:
            - number
            - 'null'
          format: double
      required:
        - external_audio_id
        - filename
        - signed_url
        - offset_ms
        - duration_ms
        - start_time_ms
        - end_time_ms
        - order
        - track_id
        - created_at_ms
        - updated_at_ms
        - import_speech_progress
      title: ProjectExternalAudioResponseModel
    ImageAnalysisStatus:
      type: string
      enum:
        - processing
        - completed
        - failed
      title: ImageAnalysisStatus
    ImageSubject:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
      required:
        - name
        - description
      title: ImageSubject
    ImageAnalysisResult:
      type: object
      properties:
        title:
          type: string
        description:
          type: string
        content_type:
          type:
            - string
            - 'null'
        mood_and_style:
          type:
            - string
            - 'null'
        composition_notes:
          type:
            - string
            - 'null'
        visible_text:
          type:
            - string
            - 'null'
          description: Readable text overlaid or shown in the image, if any.
        subjects:
          type: array
          items:
            $ref: '#/components/schemas/ImageSubject'
      required:
        - title
        - description
      title: ImageAnalysisResult
    ImageAnalysis:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/ImageAnalysisStatus'
        data:
          oneOf:
            - $ref: '#/components/schemas/ImageAnalysisResult'
            - type: 'null'
        updated_at_ms:
          type: integer
      required:
        - status
        - data
      title: ImageAnalysis
    ProjectImageResponseModel:
      type: object
      properties:
        image_id:
          type: string
        filename:
          type: string
        signed_url:
          type:
            - string
            - 'null'
        thumbnail_signed_url:
          type:
            - string
            - 'null'
        type:
          type: string
          enum:
            - image
          default: image
        source:
          type: string
          enum:
            - upload
          default: upload
        file_size_bytes:
          type: integer
        width:
          type: integer
        height:
          type: integer
        track_id:
          type: string
          default: v0
        offset_ms:
          type: integer
        duration_ms:
          type: integer
        order:
          type: string
        canvas_placement:
          $ref: '#/components/schemas/CanvasPlacement'
        animation:
          $ref: '#/components/schemas/ClipAnimation'
        opacity:
          type: number
          format: double
          default: 1
        created_at_ms:
          type: integer
        updated_at_ms:
          type: integer
        current_snapshot_id:
          type:
            - string
            - 'null'
        source_asset_id:
          type:
            - string
            - 'null'
        source_platform_asset_id:
          type:
            - string
            - 'null'
        error:
          type:
            - string
            - 'null'
        pending_task:
          oneOf:
            - $ref: '#/components/schemas/PendingClipTask'
            - type: 'null'
        analysis:
          oneOf:
            - $ref: '#/components/schemas/ImageAnalysis'
            - type: 'null'
      required:
        - image_id
        - filename
        - file_size_bytes
        - width
        - height
        - offset_ms
        - duration_ms
        - order
        - canvas_placement
        - created_at_ms
        - updated_at_ms
      title: ProjectImageResponseModel
    ProjectExtendedResponseModelAssetsItems:
      oneOf:
        - $ref: '#/components/schemas/ProjectVideoResponseModel'
        - $ref: '#/components/schemas/ProjectExternalAudioResponseModel'
        - $ref: '#/components/schemas/ProjectImageResponseModel'
      title: ProjectExtendedResponseModelAssetsItems
    ProjectVoiceResponseModel:
      type: object
      properties:
        project_voice_ref_id:
          type: string
        voice_id:
          type: string
        alias:
          type: string
        stability:
          type: number
          format: double
        similarity_boost:
          type: number
          format: double
        style:
          type: number
          format: double
        is_pinned:
          type: boolean
        use_speaker_boost:
          type: boolean
        volume_gain:
          type: number
          format: double
        speed:
          type: number
          format: double
      required:
        - project_voice_ref_id
        - voice_id
        - alias
        - stability
        - similarity_boost
        - style
        - is_pinned
        - use_speaker_boost
        - volume_gain
        - speed
      title: ProjectVoiceResponseModel
    SpeakerSeparationResponseModelStatus:
      type: string
      enum:
        - not_started
        - pending
        - completed
        - failed
      description: The status of the speaker separation.
      title: SpeakerSeparationResponseModelStatus
    UtteranceResponseModel:
      type: object
      properties:
        start:
          type: number
          format: double
          description: The start time of the utterance in seconds.
        end:
          type: number
          format: double
          description: The end time of the utterance in seconds.
      required:
        - start
        - end
      title: UtteranceResponseModel
    SpeakerResponseModel:
      type: object
      properties:
        speaker_id:
          type: string
          description: The ID of the speaker.
        duration_secs:
          type: number
          format: double
          description: The duration of the speaker segment in seconds.
        utterances:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/UtteranceResponseModel'
          description: The utterances of the speaker.
      required:
        - speaker_id
        - duration_secs
      title: SpeakerResponseModel
    SpeakerSeparationResponseModel:
      type: object
      properties:
        voice_id:
          type: string
          description: The ID of the voice.
        sample_id:
          type: string
          description: The ID of the sample.
        status:
          $ref: '#/components/schemas/SpeakerSeparationResponseModelStatus'
          description: The status of the speaker separation.
        speakers:
          type:
            - object
            - 'null'
          additionalProperties:
            $ref: '#/components/schemas/SpeakerResponseModel'
          description: The speakers of the sample.
        selected_speaker_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: The IDs of the selected speakers.
      required:
        - voice_id
        - sample_id
        - status
      title: SpeakerSeparationResponseModel
    SampleResponseModel:
      type: object
      properties:
        sample_id:
          type: string
          description: The ID of the sample.
        file_name:
          type: string
          description: The name of the sample file.
        mime_type:
          type: string
          description: The MIME type of the sample file.
        size_bytes:
          type: integer
          description: The size of the sample file in bytes.
        hash:
          type: string
          description: The hash of the sample file.
        duration_secs:
          type:
            - number
            - 'null'
          format: double
        remove_background_noise:
          type:
            - boolean
            - 'null'
        has_isolated_audio:
          type:
            - boolean
            - 'null'
        has_isolated_audio_preview:
          type:
            - boolean
            - 'null'
        speaker_separation:
          oneOf:
            - $ref: '#/components/schemas/SpeakerSeparationResponseModel'
            - type: 'null'
        trim_start:
          type:
            - integer
            - 'null'
        trim_end:
          type:
            - integer
            - 'null'
      title: SampleResponseModel
    VoiceResponseModelCategory:
      type: string
      enum:
        - generated
        - cloned
        - premade
        - professional
        - famous
        - high_quality
      description: The category of the voice.
      title: VoiceResponseModelCategory
    FineTuningResponseModelState:
      type: string
      enum:
        - not_started
        - queued
        - fine_tuning
        - fine_tuned
        - failed
        - delayed
      title: FineTuningResponseModelState
    RecordingResponseModel:
      type: object
      properties:
        recording_id:
          type: string
          description: The ID of the recording.
        mime_type:
          type: string
          description: The MIME type of the recording.
        size_bytes:
          type: integer
          description: The size of the recording in bytes.
        upload_date_unix:
          type: integer
          description: The date of the recording in Unix time.
        transcription:
          type: string
          description: The transcription of the recording.
      required:
        - recording_id
        - mime_type
        - size_bytes
        - upload_date_unix
        - transcription
      title: RecordingResponseModel
    VerificationAttemptResponseModel:
      type: object
      properties:
        text:
          type: string
          description: The text of the verification attempt.
        date_unix:
          type: integer
          description: The date of the verification attempt in Unix time.
        accepted:
          type: boolean
          description: Whether the verification attempt was accepted.
        similarity:
          type: number
          format: double
          description: The similarity of the verification attempt.
        levenshtein_distance:
          type: number
          format: double
          description: The Levenshtein distance of the verification attempt.
        recording:
          oneOf:
            - $ref: '#/components/schemas/RecordingResponseModel'
            - type: 'null'
          description: The recording of the verification attempt.
      required:
        - text
        - date_unix
        - accepted
        - similarity
        - levenshtein_distance
      title: VerificationAttemptResponseModel
    ManualVerificationFileResponseModel:
      type: object
      properties:
        file_id:
          type: string
          description: The ID of the file.
        file_name:
          type: string
          description: The name of the file.
        mime_type:
          type: string
          description: The MIME type of the file.
        size_bytes:
          type: integer
          description: The size of the file in bytes.
        upload_date_unix:
          type: integer
          description: The date of the file in Unix time.
      required:
        - file_id
        - file_name
        - mime_type
        - size_bytes
        - upload_date_unix
      title: ManualVerificationFileResponseModel
    ManualVerificationResponseModel:
      type: object
      properties:
        extra_text:
          type: string
          description: The extra text of the manual verification.
        request_time_unix:
          type: integer
          description: The date of the manual verification in Unix time.
        files:
          type: array
          items:
            $ref: '#/components/schemas/ManualVerificationFileResponseModel'
          description: The files of the manual verification.
      required:
        - extra_text
        - request_time_unix
        - files
      title: ManualVerificationResponseModel
    FineTuningResponseModel:
      type: object
      properties:
        is_allowed_to_fine_tune:
          type: boolean
          description: Whether the user is allowed to fine-tune the voice.
        state:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/FineTuningResponseModelState'
          description: The state of the fine-tuning process for each model.
        verification_failures:
          type: array
          items:
            type: string
          description: List of verification failures in the fine-tuning process.
        verification_attempts_count:
          type: integer
          description: The number of verification attempts in the fine-tuning process.
        manual_verification_requested:
          type: boolean
          description: >-
            Whether a manual verification was requested for the fine-tuning
            process.
        language:
          type:
            - string
            - 'null'
          description: The language of the fine-tuning process.
        progress:
          type:
            - object
            - 'null'
          additionalProperties:
            type: number
            format: double
          description: The progress of the fine-tuning process.
        message:
          type:
            - object
            - 'null'
          additionalProperties:
            type: string
          description: The message of the fine-tuning process.
        dataset_duration_seconds:
          type:
            - number
            - 'null'
          format: double
          description: The duration of the dataset in seconds.
        verification_attempts:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VerificationAttemptResponseModel'
          description: The number of verification attempts.
        slice_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: List of slice IDs.
        manual_verification:
          oneOf:
            - $ref: '#/components/schemas/ManualVerificationResponseModel'
            - type: 'null'
          description: The manual verification of the fine-tuning process.
        max_verification_attempts:
          type:
            - integer
            - 'null'
          description: The maximum number of verification attempts.
        next_max_verification_attempts_reset_unix_ms:
          type:
            - integer
            - 'null'
          description: >-
            The next maximum verification attempts reset time in Unix
            milliseconds.
        finetuning_state:
          description: Any type
      title: FineTuningResponseModel
    VoiceSettingsResponseModel:
      type: object
      properties:
        stability:
          type:
            - number
            - 'null'
          format: double
          default: 0.5
          description: >-
            Determines how stable the voice is and the randomness between each
            generation. Lower values introduce broader emotional range for the
            voice. Higher values can result in a monotonous voice with limited
            emotion.
        use_speaker_boost:
          type:
            - boolean
            - 'null'
          default: true
          description: >-
            This setting boosts the similarity to the original speaker. Using
            this setting requires a slightly higher computational load, which in
            turn increases latency.
        similarity_boost:
          type:
            - number
            - 'null'
          format: double
          default: 0.75
          description: >-
            Determines how closely the AI should adhere to the original voice
            when attempting to replicate it.
        style:
          type:
            - number
            - 'null'
          format: double
          default: 0
          description: >-
            Determines the style exaggeration of the voice. This setting
            attempts to amplify the style of the original speaker. It does
            consume additional computational resources and might increase
            latency if set to anything other than 0.
        speed:
          type:
            - number
            - 'null'
          format: double
          default: 1
          description: >-
            Adjusts the speed of the voice. A value of 1.0 is the default speed,
            while values less than 1.0 slow down the speech, and values greater
            than 1.0 speed it up.
      title: VoiceSettingsResponseModel
    voice_sharing_state:
      type: string
      enum:
        - enabled
        - disabled
        - copied
        - copied_disabled
      description: The status of the voice sharing.
      title: voice_sharing_state
    VoiceSharingResponseModelCategory:
      type: string
      enum:
        - generated
        - cloned
        - premade
        - professional
        - famous
        - high_quality
      description: The category of the voice.
      title: VoiceSharingResponseModelCategory
    review_status:
      type: string
      enum:
        - not_requested
        - pending
        - declined
        - allowed
        - allowed_with_changes
      description: The review status of the voice.
      title: review_status
    VoiceSharingModerationCheckResponseModel:
      type: object
      properties:
        date_checked_unix:
          type:
            - integer
            - 'null'
          description: The date the moderation check was made in Unix time.
        name_value:
          type:
            - string
            - 'null'
          description: The name value of the voice.
        name_check:
          type:
            - boolean
            - 'null'
          description: Whether the name check was successful.
        description_value:
          type:
            - string
            - 'null'
          description: The description value of the voice.
        description_check:
          type:
            - boolean
            - 'null'
          description: Whether the description check was successful.
        sample_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: A list of sample IDs.
        sample_checks:
          type:
            - array
            - 'null'
          items:
            type: number
            format: double
          description: A list of sample checks.
        captcha_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: A list of captcha IDs.
        captcha_checks:
          type:
            - array
            - 'null'
          items:
            type: number
            format: double
          description: A list of CAPTCHA check values.
      title: VoiceSharingModerationCheckResponseModel
    ReaderResourceResponseModelResourceType:
      type: string
      enum:
        - read
        - collection
      description: The type of resource.
      title: ReaderResourceResponseModelResourceType
    ReaderResourceResponseModel:
      type: object
      properties:
        resource_type:
          $ref: '#/components/schemas/ReaderResourceResponseModelResourceType'
          description: The type of resource.
        resource_id:
          type: string
          description: The ID of the resource.
      required:
        - resource_type
        - resource_id
      title: ReaderResourceResponseModel
    VoiceSharingResponseModel:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/voice_sharing_state'
          description: The status of the voice sharing.
        history_item_sample_id:
          type:
            - string
            - 'null'
          description: The sample ID of the history item.
        date_unix:
          type: integer
          description: The date of the voice sharing in Unix time.
        whitelisted_emails:
          type: array
          items:
            type: string
          description: A list of whitelisted emails.
        public_owner_id:
          type: string
          description: The ID of the public owner.
        original_voice_id:
          type: string
          description: The ID of the original voice.
        financial_rewards_enabled:
          type: boolean
          description: Whether financial rewards are enabled.
        free_users_allowed:
          type: boolean
          description: Whether free users are allowed.
        live_moderation_enabled:
          type: boolean
          description: Whether live moderation is enabled.
        rate:
          type:
            - number
            - 'null'
          format: double
          description: The rate of the voice sharing.
        fiat_rate:
          type:
            - number
            - 'null'
          format: double
          description: The rate of the voice sharing in USD per 1000 credits.
        notice_period:
          type: integer
          description: The notice period of the voice sharing.
        disable_at_unix:
          type:
            - integer
            - 'null'
          description: The date of the voice sharing in Unix time.
        voice_mixing_allowed:
          type: boolean
          description: Whether voice mixing is allowed.
        featured:
          type: boolean
          description: Whether the voice is featured.
        category:
          $ref: '#/components/schemas/VoiceSharingResponseModelCategory'
          description: The category of the voice.
        reader_app_enabled:
          type:
            - boolean
            - 'null'
          description: Whether the reader app is enabled.
        image_url:
          type:
            - string
            - 'null'
          description: The image URL of the voice.
        ban_reason:
          type:
            - string
            - 'null'
          description: The ban reason of the voice.
        liked_by_count:
          type: integer
          description: The number of likes on the voice.
        cloned_by_count:
          type: integer
          description: The number of clones on the voice.
        name:
          type: string
          description: The name of the voice.
        description:
          type:
            - string
            - 'null'
          description: The description of the voice.
        labels:
          type: object
          additionalProperties:
            type: string
          description: The labels of the voice.
        review_status:
          $ref: '#/components/schemas/review_status'
          description: The review status of the voice.
        review_message:
          type:
            - string
            - 'null'
          description: The review message of the voice.
        enabled_in_library:
          type: boolean
          description: Whether the voice is enabled in the library.
        instagram_username:
          type:
            - string
            - 'null'
          description: The Instagram username of the voice.
        twitter_username:
          type:
            - string
            - 'null'
          description: The Twitter/X username of the voice.
        youtube_username:
          type:
            - string
            - 'null'
          description: The YouTube username of the voice.
        tiktok_username:
          type:
            - string
            - 'null'
          description: The TikTok username of the voice.
        moderation_check:
          oneOf:
            - $ref: '#/components/schemas/VoiceSharingModerationCheckResponseModel'
            - type: 'null'
          description: The moderation check of the voice.
        reader_restricted_on:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ReaderResourceResponseModel'
          description: The reader restricted on of the voice.
      title: VoiceSharingResponseModel
    VerifiedVoiceLanguageResponseModel:
      type: object
      properties:
        language:
          type: string
          description: The language of the voice.
        model_id:
          type: string
          description: The voice's model ID.
        accent:
          type:
            - string
            - 'null'
          description: The voice's accent, if applicable.
        locale:
          type:
            - string
            - 'null'
          description: The voice's locale, if applicable.
        preview_url:
          type:
            - string
            - 'null'
          description: The voice's preview URL, if applicable.
      required:
        - language
        - model_id
      title: VerifiedVoiceLanguageResponseModel
    VoiceResponseModelSafetyControl:
      type: string
      enum:
        - NONE
        - BAN
        - CAPTCHA
        - ENTERPRISE_BAN
        - ENTERPRISE_CAPTCHA
      description: The safety controls of the voice.
      title: VoiceResponseModelSafetyControl
    VoiceVerificationResponseModel:
      type: object
      properties:
        requires_verification:
          type: boolean
          description: Whether the voice requires verification.
        is_verified:
          type: boolean
          description: Whether the voice has been verified.
        verification_failures:
          type: array
          items:
            type: string
          description: List of verification failures.
        verification_attempts_count:
          type: integer
          description: The number of verification attempts.
        language:
          type:
            - string
            - 'null'
          description: The language of the voice.
        verification_attempts:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VerificationAttemptResponseModel'
          description: Number of times a verification was attempted.
      required:
        - requires_verification
        - is_verified
        - verification_failures
        - verification_attempts_count
      title: VoiceVerificationResponseModel
    VoiceResponseModelRecordingQuality:
      type: string
      enum:
        - studio
        - good
        - ok
        - poor
        - bad
      description: The recording quality of the voice as determined by the review pipeline.
      title: VoiceResponseModelRecordingQuality
    VoiceResponseModelLabellingStatus:
      type: string
      enum:
        - in_review
        - review_complete
      description: The review pipeline status of the voice.
      title: VoiceResponseModelLabellingStatus
    VoiceResponseModel:
      type: object
      properties:
        voice_id:
          type: string
          description: The ID of the voice.
        name:
          type: string
          description: The name of the voice.
        samples:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/SampleResponseModel'
          description: List of samples associated with the voice.
        category:
          $ref: '#/components/schemas/VoiceResponseModelCategory'
          description: The category of the voice.
        fine_tuning:
          oneOf:
            - $ref: '#/components/schemas/FineTuningResponseModel'
            - type: 'null'
          description: Fine-tuning information for the voice.
        labels:
          type: object
          additionalProperties:
            type: string
          description: Labels associated with the voice.
        description:
          type:
            - string
            - 'null'
          description: The description of the voice.
        preview_url:
          type:
            - string
            - 'null'
          description: The preview URL of the voice.
        available_for_tiers:
          type: array
          items:
            type: string
          description: The tiers the voice is available for.
        settings:
          oneOf:
            - $ref: '#/components/schemas/VoiceSettingsResponseModel'
            - type: 'null'
          description: The settings of the voice.
        sharing:
          oneOf:
            - $ref: '#/components/schemas/VoiceSharingResponseModel'
            - type: 'null'
          description: The sharing information of the voice.
        high_quality_base_model_ids:
          type: array
          items:
            type: string
          description: The base model IDs for high-quality voices.
        verified_languages:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VerifiedVoiceLanguageResponseModel'
          description: The verified languages of the voice.
        collection_ids:
          type:
            - array
            - 'null'
          items:
            type: string
          description: The IDs of collections this voice belongs to.
        safety_control:
          oneOf:
            - $ref: '#/components/schemas/VoiceResponseModelSafetyControl'
            - type: 'null'
          description: The safety controls of the voice.
        voice_verification:
          oneOf:
            - $ref: '#/components/schemas/VoiceVerificationResponseModel'
            - type: 'null'
          description: The voice verification of the voice.
        permission_on_resource:
          type:
            - string
            - 'null'
          description: The permission on the resource of the voice.
        is_owner:
          type:
            - boolean
            - 'null'
          description: Whether the voice is owned by the user.
        is_legacy:
          type: boolean
          default: false
          description: Whether the voice is legacy.
        is_mixed:
          type: boolean
          default: false
          description: Whether the voice is mixed.
        favorited_at_unix:
          type:
            - integer
            - 'null'
          description: Timestamp when the voice was marked as favorite in Unix time.
        created_at_unix:
          type:
            - integer
            - 'null'
          description: The creation time of the voice in Unix time.
        is_bookmarked:
          type:
            - boolean
            - 'null'
          description: >-
            Whether the voice is bookmarked by the current user. Only relevant
            for community (library-copied) voices.
        recording_quality:
          oneOf:
            - $ref: '#/components/schemas/VoiceResponseModelRecordingQuality'
            - type: 'null'
          description: >-
            The recording quality of the voice as determined by the review
            pipeline.
        labelling_status:
          oneOf:
            - $ref: '#/components/schemas/VoiceResponseModelLabellingStatus'
            - type: 'null'
          description: The review pipeline status of the voice.
        recording_quality_reason:
          type:
            - string
            - 'null'
          description: >-
            The reason for the recording quality assessment, as determined by
            the review pipeline.
      required:
        - voice_id
      title: VoiceResponseModel
    ReadMetadataChapterDBModel:
      type: object
      properties:
        chapter_name:
          type: string
        word_count:
          type: integer
        char_count:
          type: integer
        starting_char_offset:
          type: integer
        has_parsed_html:
          type: boolean
          default: false
        has_summary:
          type: boolean
          default: false
        duration_seconds:
          type:
            - number
            - 'null'
          format: double
        file_number:
          type:
            - string
            - 'null'
        is_fallback_name:
          type: boolean
          default: false
        chapter_id:
          type:
            - string
            - 'null'
      required:
        - chapter_name
        - word_count
        - char_count
        - starting_char_offset
      title: ReadMetadataChapterDBModel
    DirectPublishingReadResponseModelDisplayMode:
      type: string
      enum:
        - text
        - audio-only
        - text-with-audio
      title: DirectPublishingReadResponseModelDisplayMode
    DirectPublishingReadResponseModelGenreItems:
      type: string
      enum:
        - Fantasy
        - Romance
        - Science Fiction
        - Mystery and Thriller
        - Action and Adventure
        - Dystopia
        - Business and Economics
        - Technology
        - Christian & Inspirational
        - Horror
        - Biography and Memoir
        - Education and Learning
        - History
        - Children's Literature
        - Young Adult
        - Fairy Tales and Folklore
        - Fan Fiction
        - General Fiction
        - Health and Wellness
        - Historical Fiction
        - Humor
        - Literary Classics
        - Philosophy
        - Poetry
        - Politics and Government
        - Psychology
        - Science and Nature
        - Self-Help
        - Spirituality and Religion
        - Travel
        - True Crime
        - Other
      title: DirectPublishingReadResponseModelGenreItems
    DirectPublishingReadResponseModelTargetAudience:
      type: string
      enum:
        - children
        - young adult
        - adult
        - all ages
      title: DirectPublishingReadResponseModelTargetAudience
    ReadLegalTerms:
      type: object
      properties:
        terms:
          type:
            - string
            - 'null'
        start_date:
          type:
            - string
            - 'null'
        end_date:
          type:
            - string
            - 'null'
      title: ReadLegalTerms
    Contributor:
      type: object
      properties:
        name:
          type: string
        role:
          type: string
        bio:
          type:
            - string
            - 'null'
        profile_id:
          type:
            - string
            - 'null'
      required:
        - name
        - role
      title: Contributor
    DirectPublishingReadResponseModelPayoutType:
      type: string
      enum:
        - none
        - engagement_based
        - fixed_payout
      title: DirectPublishingReadResponseModelPayoutType
    PreviewAudioDBModel:
      type: object
      properties:
        voice_id:
          type:
            - string
            - 'null'
        text:
          type:
            - string
            - 'null'
        audio_url:
          type: string
        hls_manifest_url:
          type:
            - string
            - 'null'
        dash_manifest_url:
          type:
            - string
            - 'null'
        is_auto_generated:
          type:
            - boolean
            - 'null'
          default: false
        generated_at_unix:
          type:
            - integer
            - 'null'
      required:
        - audio_url
      title: PreviewAudioDBModel
    SampleConfigDbModelParentType:
      type: string
      enum:
        - read
        - collection
      title: SampleConfigDbModelParentType
    SampleConfigDBModel:
      type: object
      properties:
        is_sample:
          type: boolean
          default: false
        parent_id:
          type:
            - string
            - 'null'
        parent_type:
          oneOf:
            - $ref: '#/components/schemas/SampleConfigDbModelParentType'
            - type: 'null'
        chapter_ids:
          type:
            - array
            - 'null'
          items:
            type: string
      title: SampleConfigDBModel
    ReviewResponseModelReviewStatus:
      type: string
      enum:
        - approved
        - edits_required
        - rejected
      title: ReviewResponseModelReviewStatus
    ReviewResponseModelRejectReasonsItems:
      type: string
      enum:
        - lacks_structure
        - doesnt_open
        - not_literary_work
        - language_not_supported
        - too_short
        - duplicate
        - promotional
        - formatting_issues
        - low_quality
        - metadata_incomplete
        - metadata_inaccurate
        - typos
        - review_error
        - spam
        - legal_violation
        - content_policy
        - public_domain
        - other
      title: ReviewResponseModelRejectReasonsItems
    ReviewResponseModel:
      type: object
      properties:
        review_status:
          $ref: '#/components/schemas/ReviewResponseModelReviewStatus'
        reviewed_at_unix:
          type: integer
        reviewed_by:
          type:
            - string
            - 'null'
        reject_reasons:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/ReviewResponseModelRejectReasonsItems'
        scores_breakdown:
          type:
            - object
            - 'null'
          additionalProperties:
            type: integer
        rejected_details:
          type:
            - string
            - 'null'
        explanation:
          type:
            - string
            - 'null'
      required:
        - review_status
        - reviewed_at_unix
      title: ReviewResponseModel
    DirectPublishingReadResponseModel:
      type: object
      properties:
        read_id:
          type: string
        created_at_unix:
          type: integer
        updated_at_unix:
          type: integer
        word_count:
          type: integer
        char_count:
          type: integer
        chapters:
          type: array
          items:
            $ref: '#/components/schemas/ReadMetadataChapterDBModel'
        title:
          type:
            - string
            - 'null'
        author:
          type:
            - string
            - 'null'
        description:
          type:
            - string
            - 'null'
        article_image_url:
          type:
            - string
            - 'null'
        language:
          type:
            - string
            - 'null'
        locale:
          type:
            - string
            - 'null'
        display_mode:
          oneOf:
            - $ref: >-
                #/components/schemas/DirectPublishingReadResponseModelDisplayMode
            - type: 'null'
        genre:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/DirectPublishingReadResponseModelGenreItems'
        fiction:
          type:
            - string
            - 'null'
        content_type:
          type:
            - string
            - 'null'
        original_file_type:
          type:
            - string
            - 'null'
        target_audience:
          oneOf:
            - $ref: >-
                #/components/schemas/DirectPublishingReadResponseModelTargetAudience
            - type: 'null'
        mature_content:
          type:
            - boolean
            - 'null'
        safesearch_adult:
          type:
            - boolean
            - 'null'
        origin:
          type:
            - string
            - 'null'
        publication_date:
          type:
            - string
            - 'null'
        isbn:
          type:
            - string
            - 'null'
        ean:
          type:
            - string
            - 'null'
        legal_terms:
          oneOf:
            - $ref: '#/components/schemas/ReadLegalTerms'
            - type: 'null'
        content_guidelines_terms:
          oneOf:
            - $ref: '#/components/schemas/ReadLegalTerms'
            - type: 'null'
        last_updated_from_project_unix:
          type:
            - integer
            - 'null'
        publishing_project_id:
          type:
            - string
            - 'null'
        publishing_state:
          type: string
          default: published
        publisher_profile_id:
          type:
            - string
            - 'null'
        quality_score:
          type:
            - integer
            - 'null'
        publisher:
          type:
            - string
            - 'null'
        copyright:
          type:
            - string
            - 'null'
        subtitle:
          type:
            - string
            - 'null'
        distribution_territories:
          type:
            - array
            - 'null'
          items:
            type: string
        edition:
          type:
            - string
            - 'null'
        contributors:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/Contributor'
        payout_type:
          oneOf:
            - $ref: '#/components/schemas/DirectPublishingReadResponseModelPayoutType'
            - type: 'null'
        list_price:
          type:
            - number
            - 'null'
          format: double
        currency:
          type:
            - string
            - 'null'
          enum:
            - usd
        original_audio_project_export_id:
          type:
            - string
            - 'null'
        original_audio_document_id:
          type:
            - string
            - 'null'
        series_id:
          type:
            - string
            - 'null'
        volume:
          type:
            - integer
            - 'null'
        published_at_unix:
          type:
            - integer
            - 'null'
        read_slug:
          type:
            - string
            - 'null'
        preview_audio_object:
          oneOf:
            - $ref: '#/components/schemas/PreviewAudioDBModel'
            - type: 'null'
        sample_config:
          oneOf:
            - $ref: '#/components/schemas/SampleConfigDBModel'
            - type: 'null'
        review:
          oneOf:
            - $ref: '#/components/schemas/ReviewResponseModel'
            - type: 'null'
        voice_id:
          type:
            - string
            - 'null'
        can_use_assistant:
          type: boolean
          default: true
        is_voice_changer_on:
          type: boolean
          default: false
      required:
        - read_id
        - created_at_unix
        - updated_at_unix
        - word_count
        - char_count
        - chapters
      title: DirectPublishingReadResponseModel
    ProjectExtendedResponseModel:
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
            - $ref: '#/components/schemas/ProjectExtendedResponseModelTargetAudience'
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
          $ref: '#/components/schemas/ProjectExtendedResponseModelAccessLevel'
          description: The access level of the project.
        fiction:
          oneOf:
            - $ref: '#/components/schemas/ProjectExtendedResponseModelFiction'
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
            - $ref: '#/components/schemas/ProjectExtendedResponseModelSourceType'
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
            - $ref: '#/components/schemas/ProjectExtendedResponseModelAspectRatio'
            - type: 'null'
          description: The aspect ratio of the project.
        agent_settings:
          oneOf:
            - $ref: '#/components/schemas/StudioAgentSettingsModel'
            - type: 'null'
          description: Agent-related settings for the project
        quality_preset:
          $ref: '#/components/schemas/QualityPresetType'
          description: The quality preset level of the project.
        chapters:
          type: array
          items:
            $ref: '#/components/schemas/ChapterResponseModel'
          description: List of chapters of the project and their metadata.
        pronunciation_dictionary_versions:
          type: array
          items:
            $ref: '#/components/schemas/PronunciationDictionaryVersionResponseModel'
          description: >-
            List of pronunciation dictionary versions of the project and their
            metadata.
        pronunciation_dictionary_locators:
          type: array
          items:
            $ref: '#/components/schemas/PronunciationDictionaryLocatorResponseModel'
          description: List of pronunciation dictionary locators.
        apply_text_normalization:
          $ref: >-
            #/components/schemas/ProjectExtendedResponseModelApplyTextNormalization
          description: Whether text normalization is applied to the project.
        experimental:
          type: object
          additionalProperties:
            description: Any type
          description: Experimental features for the project.
        assets:
          type: array
          items:
            $ref: '#/components/schemas/ProjectExtendedResponseModelAssetsItems'
          description: List of uploaded assets e.g. videos, audios.
        voices:
          type: array
          items:
            $ref: '#/components/schemas/ProjectVoiceResponseModel'
          description: List of configured project voices.
        base_voices:
          type:
            - array
            - 'null'
          items:
            $ref: '#/components/schemas/VoiceResponseModel'
          description: List of voices used by the project.
        publishing_read:
          oneOf:
            - $ref: '#/components/schemas/DirectPublishingReadResponseModel'
            - type: 'null'
          description: The ElevenReader data if the book was published.
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
        - quality_preset
        - chapters
        - pronunciation_dictionary_versions
        - pronunciation_dictionary_locators
        - apply_text_normalization
        - assets
        - voices
        - default_title_voice_id
        - default_paragraph_voice_id
      title: ProjectExtendedResponseModel
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



**Response**

```json
{
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
  "quality_preset": "standard",
  "chapters": [
    {
      "chapter_id": "aw1NgEzBg83R7vgmiJt6",
      "name": "Chapter 1",
      "can_be_downloaded": true,
      "state": "converting",
      "last_conversion_date_unix": 1714204800,
      "conversion_progress": 0.5,
      "statistics": {
        "characters_unconverted": 1000,
        "characters_converted": 500,
        "paragraphs_converted": 20,
        "paragraphs_unconverted": 10,
        "credits_needed_to_convert": 1000,
        "voice_statistics": [
          {
            "project_voice_ref_id": "voice123",
            "characters_unconverted": 600,
            "characters_converted": 300,
            "voice_id": "voice123"
          },
          {
            "project_voice_ref_id": "voice456",
            "characters_unconverted": 400,
            "characters_converted": 200,
            "voice_id": "voice456"
          }
        ]
      },
      "last_conversion_error": "Error message"
    }
  ],
  "pronunciation_dictionary_versions": [],
  "pronunciation_dictionary_locators": [],
  "apply_text_normalization": "auto",
  "assets": [],
  "voices": [],
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
  "public_share_id": "abc123def456789",
  "experimental": {},
  "base_voices": []
}
```

**SDK Code**

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.studio.projects.get("project_id", {});
}
main();

```

```python
from elevenlabs import ElevenLabs

client = ElevenLabs()

client.studio.projects.get(
    project_id="project_id",
)

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.elevenlabs.io/v1/studio/projects/project_id"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.elevenlabs.io/v1/studio/projects/project_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.elevenlabs.io/v1/studio/projects/project_id")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.elevenlabs.io/v1/studio/projects/project_id');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/projects/project_id");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/projects/project_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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
