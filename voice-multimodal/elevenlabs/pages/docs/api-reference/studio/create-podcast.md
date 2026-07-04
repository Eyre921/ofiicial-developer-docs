---
title: "Create Podcast"
source: https://elevenlabs.io/docs/api-reference/studio/create-podcast.md
path: docs/api-reference/studio/create-podcast
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Create Podcast

POST https://api.elevenlabs.io/v1/studio/podcasts
Content-Type: application/json

Create and auto-convert a podcast project. Currently, the LLM cost is covered by us but you will still be charged for the audio generation. In the future, you will be charged for both the LLM and audio generation costs.

Reference: https://elevenlabs.io/docs/api-reference/studio/create-podcast

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /v1/studio/podcasts:
    post:
      operationId: create_podcast
      summary: Create Podcast
      description: >-
        Create and auto-convert a podcast project. Currently, the LLM cost is
        covered by us but you will still be charged for the audio generation. In
        the future, you will be charged for both the LLM and audio generation
        costs.
      tags:
        - studio
      parameters:
        - name: xi-api-key
          in: header
          required: false
          schema:
            type: string
        - name: safety-identifier
          in: header
          description: >-
            Used for moderation. Your workspace must be allowlisted to use this
            feature.
          required: false
          schema:
            type:
              - string
              - 'null'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PodcastProjectResponseModel'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Body_Create_podcast_v1_studio_podcasts_post'
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
    PodcastConversationModeData:
      type: object
      properties:
        host_voice_id:
          type: string
          description: The ID of the host voice.
        guest_voice_id:
          type: string
          description: The ID of the guest voice.
      required:
        - host_voice_id
        - guest_voice_id
      title: PodcastConversationModeData
    PodcastConversationMode:
      type: object
      properties:
        type:
          type: string
          enum:
            - conversation
          description: The type of podcast to create.
        conversation:
          $ref: '#/components/schemas/PodcastConversationModeData'
          description: The voice settings for the conversation.
      required:
        - type
        - conversation
      title: PodcastConversationMode
    PodcastBulletinModeData:
      type: object
      properties:
        host_voice_id:
          type: string
          description: The ID of the host voice.
      required:
        - host_voice_id
      title: PodcastBulletinModeData
    PodcastBulletinMode:
      type: object
      properties:
        type:
          type: string
          enum:
            - bulletin
          description: The type of podcast to create.
        bulletin:
          $ref: '#/components/schemas/PodcastBulletinModeData'
          description: The voice settings for the bulletin.
      required:
        - type
        - bulletin
      title: PodcastBulletinMode
    BodyCreatePodcastV1StudioPodcastsPostMode:
      oneOf:
        - $ref: '#/components/schemas/PodcastConversationMode'
        - $ref: '#/components/schemas/PodcastBulletinMode'
      description: >-
        The type of podcast to generate. Can be 'conversation', an interaction
        between two voices, or 'bulletin', a monologue.
      title: BodyCreatePodcastV1StudioPodcastsPostMode
    PodcastTextSource:
      type: object
      properties:
        type:
          type: string
          enum:
            - text
          description: The type of source to create.
        text:
          type: string
          description: The text to create the podcast from.
      required:
        - type
        - text
      title: PodcastTextSource
    PodcastURLSource:
      type: object
      properties:
        type:
          type: string
          enum:
            - url
          description: The type of source to create.
        url:
          type: string
          description: The URL to create the podcast from.
      required:
        - type
        - url
      title: PodcastURLSource
    BodyCreatePodcastV1StudioPodcastsPostSourceOneOf2Items:
      oneOf:
        - $ref: '#/components/schemas/PodcastTextSource'
        - $ref: '#/components/schemas/PodcastURLSource'
      title: BodyCreatePodcastV1StudioPodcastsPostSourceOneOf2Items
    BodyCreatePodcastV1StudioPodcastsPostSource2:
      type: array
      items:
        $ref: >-
          #/components/schemas/BodyCreatePodcastV1StudioPodcastsPostSourceOneOf2Items
      title: BodyCreatePodcastV1StudioPodcastsPostSource2
    BodyCreatePodcastV1StudioPodcastsPostSource:
      oneOf:
        - $ref: '#/components/schemas/PodcastTextSource'
        - $ref: '#/components/schemas/PodcastURLSource'
        - $ref: '#/components/schemas/BodyCreatePodcastV1StudioPodcastsPostSource2'
      description: The source content for the Podcast.
      title: BodyCreatePodcastV1StudioPodcastsPostSource
    QualityPresetType:
      type: string
      enum:
        - standard
        - high
        - ultra
        - ultra_lossless
      default: standard
      title: QualityPresetType
    BodyCreatePodcastV1StudioPodcastsPostDurationScale:
      type: string
      enum:
        - short
        - default
        - long
      default: default
      description: |
        Duration of the generated podcast. Must be one of:
        short - produces podcasts shorter than 3 minutes.
        default - produces podcasts roughly between 3-7 minutes.
        long - produces podcasts longer than 7 minutes.
      title: BodyCreatePodcastV1StudioPodcastsPostDurationScale
    BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization:
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
            
      title: BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization
    Body_Create_podcast_v1_studio_podcasts_post:
      type: object
      properties:
        model_id:
          type: string
          description: >-
            The ID of the model to be used for this Studio project, you can
            query GET /v1/models to list all available models.
        mode:
          $ref: '#/components/schemas/BodyCreatePodcastV1StudioPodcastsPostMode'
          description: >-
            The type of podcast to generate. Can be 'conversation', an
            interaction between two voices, or 'bulletin', a monologue.
        source:
          $ref: '#/components/schemas/BodyCreatePodcastV1StudioPodcastsPostSource'
          description: The source content for the Podcast.
        quality_preset:
          $ref: '#/components/schemas/QualityPresetType'
          default: standard
          description: >
            Output quality of the generated audio. Must be one of:

            'standard' - standard output format, 128kbps with 44.1kHz sample
            rate.

            'high' - high quality output format, 192kbps with 44.1kHz sample
            rate and major improvements on our side.

            'ultra' - ultra quality output format, 192kbps with 44.1kHz sample
            rate and highest improvements on our side.

            'ultra_lossless' - ultra quality output format, 705.6kbps with
            44.1kHz sample rate and highest improvements on our side in a fully
            lossless format.
        duration_scale:
          $ref: >-
            #/components/schemas/BodyCreatePodcastV1StudioPodcastsPostDurationScale
          default: default
          description: |
            Duration of the generated podcast. Must be one of:
            short - produces podcasts shorter than 3 minutes.
            default - produces podcasts roughly between 3-7 minutes.
            long - produces podcasts longer than 7 minutes.
        language:
          type:
            - string
            - 'null'
          description: >-
            An optional language of the Studio project. Two-letter language code
            (ISO 639-1).
        intro:
          type:
            - string
            - 'null'
          description: >-
            The intro text that will always be added to the beginning of the
            podcast.
        outro:
          type:
            - string
            - 'null'
          description: The outro text that will always be added to the end of the podcast.
        instructions_prompt:
          type:
            - string
            - 'null'
          description: >-
            Additional instructions prompt for the podcast generation used to
            adjust the podcast's style and tone.
        highlights:
          type:
            - array
            - 'null'
          items:
            type: string
          description: >-
            A brief summary or highlights of the Studio project's content,
            providing key points or themes. This should be between 10 and 70
            characters.
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
                
        apply_text_normalization:
          oneOf:
            - $ref: >-
                #/components/schemas/BodyCreatePodcastV1StudioPodcastsPostApplyTextNormalization
            - type: 'null'
          description: |2-

                This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'.
                When set to 'auto', the system will automatically decide whether to apply text normalization
                (e.g., spelling out numbers). With 'on', text normalization will always be applied, while
                with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.
                
      required:
        - model_id
        - mode
        - source
      title: Body_Create_podcast_v1_studio_podcasts_post
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
    PodcastProjectResponseModel:
      type: object
      properties:
        project:
          $ref: '#/components/schemas/ProjectResponseModel'
          description: The project associated with the created podcast.
      required:
        - project
      title: PodcastProjectResponseModel
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
  "model_id": "eleven_multilingual_v2",
  "mode": {
    "conversation": {
      "guest_voice_id": "bYTqZQo3Jz7LQtmGTgwi",
      "host_voice_id": "6lCwbsX1yVjD49QmpkTR"
    },
    "type": "conversation"
  },
  "source": {
    "type": "url",
    "url": "https://en.wikipedia.org/wiki/Cognitive_science"
  }
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
    await client.studio.createPodcast({
        modelId: "eleven_multilingual_v2",
        mode: {
            type: "conversation",
            conversation: {
                guestVoiceId: "bYTqZQo3Jz7LQtmGTgwi",
                hostVoiceId: "6lCwbsX1yVjD49QmpkTR",
            },
        },
        source: {
            type: "url",
            url: "https://en.wikipedia.org/wiki/Cognitive_science",
        },
    });
}
main();

```

```python
from elevenlabs import ElevenLabs, PodcastConversationModeData, PodcastUrlSource
from elevenlabs.studio import BodyCreatePodcastV1StudioPodcastsPostMode_Conversation

client = ElevenLabs()

client.studio.create_podcast(
    model_id="eleven_multilingual_v2",
    mode=BodyCreatePodcastV1StudioPodcastsPostMode_Conversation(
        conversation=PodcastConversationModeData(
            guest_voice_id="bYTqZQo3Jz7LQtmGTgwi",
            host_voice_id="6lCwbsX1yVjD49QmpkTR",
        ),
    ),
    source=PodcastUrlSource(
        type="url",
        url="https://en.wikipedia.org/wiki/Cognitive_science",
    ),
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

	url := "https://api.elevenlabs.io/v1/studio/podcasts"

	payload := strings.NewReader("{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"conversation\": {\n      \"guest_voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\",\n      \"host_voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    },\n    \"type\": \"conversation\"\n  },\n  \"source\": {\n    \"type\": \"url\",\n    \"url\": \"https://en.wikipedia.org/wiki/Cognitive_science\"\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Content-Type", "application/json")

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

url = URI("https://api.elevenlabs.io/v1/studio/podcasts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"conversation\": {\n      \"guest_voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\",\n      \"host_voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    },\n    \"type\": \"conversation\"\n  },\n  \"source\": {\n    \"type\": \"url\",\n    \"url\": \"https://en.wikipedia.org/wiki/Cognitive_science\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.elevenlabs.io/v1/studio/podcasts")
  .header("Content-Type", "application/json")
  .body("{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"conversation\": {\n      \"guest_voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\",\n      \"host_voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    },\n    \"type\": \"conversation\"\n  },\n  \"source\": {\n    \"type\": \"url\",\n    \"url\": \"https://en.wikipedia.org/wiki/Cognitive_science\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.elevenlabs.io/v1/studio/podcasts', [
  'body' => '{
  "model_id": "eleven_multilingual_v2",
  "mode": {
    "conversation": {
      "guest_voice_id": "bYTqZQo3Jz7LQtmGTgwi",
      "host_voice_id": "6lCwbsX1yVjD49QmpkTR"
    },
    "type": "conversation"
  },
  "source": {
    "type": "url",
    "url": "https://en.wikipedia.org/wiki/Cognitive_science"
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.elevenlabs.io/v1/studio/podcasts");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model_id\": \"eleven_multilingual_v2\",\n  \"mode\": {\n    \"conversation\": {\n      \"guest_voice_id\": \"bYTqZQo3Jz7LQtmGTgwi\",\n      \"host_voice_id\": \"6lCwbsX1yVjD49QmpkTR\"\n    },\n    \"type\": \"conversation\"\n  },\n  \"source\": {\n    \"type\": \"url\",\n    \"url\": \"https://en.wikipedia.org/wiki/Cognitive_science\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "model_id": "eleven_multilingual_v2",
  "mode": [
    "conversation": [
      "guest_voice_id": "bYTqZQo3Jz7LQtmGTgwi",
      "host_voice_id": "6lCwbsX1yVjD49QmpkTR"
    ],
    "type": "conversation"
  ],
  "source": [
    "type": "url",
    "url": "https://en.wikipedia.org/wiki/Cognitive_science"
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.elevenlabs.io/v1/studio/podcasts")! as URL,
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
